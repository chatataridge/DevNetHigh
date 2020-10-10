import requests
from requests.auth import HTTPBasicAuth
from dnac_config import DNAC, DNAC_PORT, DNAC_USER, DNAC_PASSWORD


def get_auth_token():
    """
    Building out Auth request. Using requests.post to make a call to the Auth Endpoint
    """
    url = 'https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token'       # Endpoint URL
    resp = requests.post(url, verify=False, auth=HTTPBasicAuth(
        DNAC_USER, DNAC_PASSWORD))  # Make the POST Request
    token = resp.json()['Token']    # Retrieve the Token from the returned JSON
    verify = False
    print("Token Retrieved: {}".format(token))  # Print out the Token
    return token    # Create a return statement to send the token back for later use



token = get_auth_token()  # Get a Token
url = "https://sandboxdnac.cisco.com/api/v1/network-device"  # Network Device endpoint
# Build header Info
verify = False
hdr = {'x-auth-token': token, 'content-type': 'application/json'}
resp = requests.get(url, headers=hdr, verify = False)  # Make the Get Request
device_list = resp.json()  # capture the data from the controller
print_device_list(device_list)  # pretty print the data we want

if __name__ == "__main__":
  get_device_list()
