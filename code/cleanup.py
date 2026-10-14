import subprocess
import settings

try:
    # remove all log files
    print(f"Removing log files")
    result = subprocess.run(["rm", "-f", "logfile.log"], check=True)
    command = f"kubectl delete pods -n default"
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print(f"Log files removed")

    # delete all pods
    print("deleting all pods")
    command = f"kubectl delete pods --all"
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print("all pods deleted")

    # remove all worker nodes
    for worker in settings.NODES[1:]:
        print(f"deleting {worker}")
        command = f"kubectl delete node {worker}"
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(f"{worker} deleted")
except:
    print(f"Error while deleting pods and logs")
print(f"Cleanup successful")