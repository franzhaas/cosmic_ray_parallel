import subprocess
import re

def create_report(filename):
    dump = subprocess.run("cosmic-ray dump {}".format(filename), stdout=subprocess.PIPE, shell=True)
    report_creator = subprocess.Popen("cr-report --full", stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    stdout, stderr = report_creator.communicate(dump.stdout)
    stdout = re.sub(r"job ID [0-9a-fA-F]+\:", "job ID 0000:", stdout.decode())
    stdout = re.sub(r" at 0x[0-9a-fA-F]+\>", "at 0xDEADBEEF>", stdout)
    return {"return code": report_creator.wait(), "stdout": stdout, "stderr": stderr}
