import base64
import requests
import json
import csv

#Add your api key below for that variable and it's ready to use.
apiKey = "add_your_api_key_here"
loginString = apiKey + ":"
encodedBytes = base64.b64encode(loginString.encode())
encodedUserPassSequence = str(encodedBytes, 'utf-8')
authorizationHeader = "Basic " + encodedUserPassSequence

apiEndpoint_Url = "https://cloudgz.gravityzone.bitdefender.com/api/v1.0/jsonrpc/packages"

request = {
    "params": {},
    "jsonrpc": "2.0",
    "method": "getInstallationLinks",
    "id": "426db9bb-e92a-4824-a21b-bba6b62d0a18"
}

result = requests.post(apiEndpoint_Url, json=request, verify=True, headers={"Content-Type": "application/json", "Authorization": authorizationHeader})

# Check if the request was successful
if result.status_code == 200:
    response_data = result.json()

    # Extract the "result" field from the response
    packages = response_data.get("result", [])

    # Define the file name for the CSV file
    csv_filename = "packages.csv"

    # Write the extracted data to a CSV file
    with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["packageName", "companyName", "companyId", "installLinkWindows", "installLinkMac", "installLinkMacArm", "installLinkMacDownloader", "installLinkLinux", "fullKitWindowsX32", "fullKitWindowsX64", "fullKitWindowsArm64", "fullKitLinuxX32", "fullKitLinuxX64", "fullKitLinuxArm64"])  # Define the fieldnames
        writer.writeheader()  # Write the header row

        # Write each package as a row in the CSV file
        for package in packages:
            writer.writerow({
                "packageName": package.get("packageName"),
                "companyName": package.get("companyName"),
                "companyId": package.get("companyId"),
                "installLinkWindows": package.get("installLinkWindows"),
                "installLinkMac": package.get("installLinkMac"),
                "installLinkMacArm": package.get("installLinkMacArm"),
                "installLinkMacDownloader": package.get("installLinkMacDownloader"),
                "installLinkLinux": package.get("installLinkLinux"),
                "fullKitWindowsX32": package.get("fullKitWindowsX32"),
                "fullKitWindowsX64": package.get("fullKitWindowsX64"),
                "fullKitWindowsArm64": package.get("fullKitWindowsArm64"),
                "fullKitLinuxX32": package.get("fullKitLinuxX32"),
                "fullKitLinuxX64": package.get("fullKitLinuxX64"),
                "fullKitLinuxArm64": package.get("fullKitLinuxArm64")
            })

    print(f"CSV file '{csv_filename}' has been created successfully.")
else:
    print("Failed to retrieve packages:", result.text)
