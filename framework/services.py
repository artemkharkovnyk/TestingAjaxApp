import threading
import subprocess
import time
import os
import signal
from framework.logger import appium_logger as logger


class Appium:
    """
    A class to manage the Appium server instance for mobile automation testing.
    """
    def __init__(self) -> None:
        """
        Initialize an Appium instance.

        This initializes the Appium process and logging thread.
        """
        self.proc = None
        self.stop_logging = threading.Event()
        logger.info('Appium instance created')

    def start(self) -> None:
        """
        Start the Appium server.

        This method starts the Appium server process and its logging thread.
        """
        cmd = ['appium', '-a', '0.0.0.0', '-p', '4723', '--allow-insecure', 'adb_shell']
        self.port = 4723
        self.proc = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdin=subprocess.PIPE,
            shell=True
        )
        time.sleep(10)
        self.logging_thread = threading.Thread(target=self._logging)
        self.logging_thread.start()
        self._get_listener_pid()
        if self.is_running():
            logger.info('Appium server is running')
        else:
            logger.error("Appium server isn't running")
            raise Exception("Appium server isn't running")

    def is_running(self) -> bool:
        """
        Check if the Appium server is running. Check only exising open proces.

        Returns:
            bool: True if the Appium server is running, otherwise False.
        """
        return self.proc.poll() is None

    def _logging(self):
        """
        Log Appium process output.

        This method logs the standard output of the Appium process.
        """
        if self.proc is None:
            logger.error("Appium process is not running")
            raise Exception("Appium server isn't running")

        while not self.stop_logging.is_set() and self.proc.poll() is None:  
            stdout_line = self.proc.stdout.readline().strip()
            if stdout_line:
                logger.info(f'Appium process stdout: {stdout_line}')
            time.sleep(1) 

    def _get_listener_pid(self) -> int:
        """
        Get the listener process PID.

        This method retrieves the PID of the Appium listener process.
        """
        logger.warning(str(['lsof', '-t', '-i', f':{self.port}']))
        output = subprocess.check_output(['lsof', '-t', '-i', f':{self.port}'])
        logger.warning(output)
        self._listener_pid = int(output.strip())
               

    def stop(self) -> None:
        """
        Stop the Appium server.

        This method stops the Appium server process and the logging thread.
        """
        if self.proc:
            self.proc.terminate()
            self.proc.wait()
            self.proc = None
            if self.logging_thread:
                self.stop_logging.set()
                self.logging_thread.join()
            try:
                os.kill(self._listener_pid, signal.SIGTERM)
                time.sleep(5)
                logger.info(f'Appium server stopped')
            except ProcessLookupError:
                logger.warn(f"Didn't stopped listener porcess. No process found with PID {self._listener_pid}.")
            except Exception as e:
                logger.error(f"An error occurred while trying to kill the listner process: {e}")
           
        