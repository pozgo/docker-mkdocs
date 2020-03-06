import shlex
import subprocess


class Command:
    """Representation of a shell command with its execution and output.

    This class enables the ability to wrap any command line utility, run it
    and capture its output for further processing.

    Attributes:
        executable_with_arguments (str): Full command line as it would typed
        in a shell, including arguments, flags...
        cmd_output (str): the captured output of the command after it's run
        suppress_output (bool): whether or not to output in the console the
        result of running this command

    Note:
        See https://janakiev.com/blog/python-shell-commands/ for more details

    """
    def __init__(self, executable_with_arguments: str,
                 suppress_output: bool = False,
                 working_dir: str = None) -> None:
        self.executable_with_arguments = executable_with_arguments
        self.suppress_output = suppress_output
        self.cmd_output = ""
        self.working_dir = working_dir

    def run(self):
        """ Executes a command instance, printing its progress
        on stdout as it runs.

        The result of the command is buffered as a string and saved.
        Any errors in execution are surfaced and redirected
        to stdout for easy identification

        """
        commandline = shlex.split(self.executable_with_arguments)
        print(f"Executing [ {self.executable_with_arguments} ]:\n")

        if self.working_dir is not None:
            print(f"About to start process at working dir {self.working_dir}")
            # redirect stderr to stdout
            process = subprocess.Popen(commandline,
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.STDOUT,
                                       universal_newlines=True,
                                       cwd=self.working_dir)
        else:
            # redirect stderr to stdout
            process = subprocess.Popen(commandline,
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.STDOUT,
                                       universal_newlines=True)

        result: str = ""

        while True:
            output = process.stdout.readline()
            line = str(output.strip())
            result += line + "\n"
            print(line)
            return_code = process.poll()
            if return_code is not None:
                if not self.suppress_output:
                    print('Process finished with return code', return_code)
                    print(f"Output: \n{result}")
                self.cmd_output = result
                break





