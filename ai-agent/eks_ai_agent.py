import subprocess

def run_command(command):
    result = subprocess.getoutput(command)
    return result

def analyze_pods(namespace):
    print("\nChecking pods...\n")
    pods = run_command(f"kubectl get pods -n {namespace}")
    print(pods)

    if "CrashLoopBackOff" in pods:
        print("\nIssue Found: Pod is crashing")
        print("Recommendation:")
        print(f"kubectl logs -n {namespace} <pod-name>")
        print(f"kubectl describe pod -n {namespace} <pod-name>")

    elif "ImagePullBackOff" in pods or "ErrImagePull" in pods:
        print("\nIssue Found: Image pull issue")
        print("Recommendation:")
        print("Check Docker image name and tag")
        print("Check Docker Hub image availability")

    elif "Pending" in pods:
        print("\nIssue Found: Pod pending")
        print("Recommendation:")
        print("Check node capacity, PVC, taints, or scheduling issue")
        print(f"kubectl describe pod -n {namespace} <pod-name>")

    else:
        print("\nNo major pod issue found")

def analyze_services(namespace):
    print("\nChecking services...\n")
    services = run_command(f"kubectl get svc -n {namespace}")
    print(services)

    if "LoadBalancer" in services and "<pending>" in services:
        print("\nIssue Found: LoadBalancer pending")
        print("Recommendation:")
        print("Check AWS LoadBalancer provisioning and subnet tags")
    else:
        print("\nService looks fine")

def analyze_logs(namespace, app_label):
    print("\nChecking logs...\n")
    logs = run_command(f"kubectl logs -n {namespace} -l app={app_label} --tail=30")
    print(logs)

    if "error" in logs.lower():
        print("\nIssue Found: Error found in logs")
        print("Recommendation:")
        print("Check application environment variables and database connection")
    else:
        print("\nNo major log error found")

def generate_report(namespace, app_label):
    print("\n==============================")
    print("AI EKS Operations Report")
    print("==============================")

    analyze_pods(namespace)
    analyze_services(namespace)
    analyze_logs(namespace, app_label)

    print("\nUseful troubleshooting commands:")
    print(f"kubectl get all -n {namespace}")
    print(f"kubectl describe pod -n {namespace} <pod-name>")
    print(f"kubectl logs -n {namespace} -l app={app_label}")
    print(f"kubectl get events -n {namespace} --sort-by=.metadata.creationTimestamp")

namespace = input("Enter namespace: ")
app_label = input("Enter app label: ")

generate_report(namespace, app_label)
