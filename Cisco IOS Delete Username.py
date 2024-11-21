##########################################################################
################# Remove a Username Script ###############################
##########################################################################

from netmiko import ConnectHandler
from netmiko.exceptions import NetMikoTimeoutException
from netmiko.exceptions import SSHException
from netmiko.exceptions import AuthenticationException
from socket import error as socket_error
import errno
import re
import logging


#Enable Netmiko logging level DEBUG - Optional - Make sure the .log file exists in the destination folder.
#logging.basicConfig(filename=r'C:\Users\YOUR_PATH\netmiko_global.log', level=logging.DEBUG)
#logger = logging.getLogger("netmiko")


def remove_username(device):
    connection = ConnectHandler(**device)
    connection.enable()
    delete_output = connection.send_command(
    command_string='config terminal',
    expect_string=r"#",
    strip_command=False,
    strip_prompt=False
    )
    delete_output += connection.send_command(
    command_string='no username USERNAME_TO_DELETE_CHANGE_ME',
    expect_string=r"Do you want to continue",
    strip_command=False,
    strip_prompt=False
    )
    delete_output += connection.send_command(
    command_string='\n',
    expect_string=r"#",
    strip_prompt=False,
    strip_command=False
    )
    delete_output += connection.send_command(
    command_string='end',
    expect_string=r"#",
    strip_prompt=False,
    strip_command=False
    )
    print(delete_output)
    save_confg = connection.save_config()
    print(save_confg)
    connection.disconnect()


####################################################################################################
#Hardware credentials

#Username and password
username = 'YOUR_USERNAME'
password = 'YOUR_PASSWORD'


devices = [
    {'device_type': 'cisco_ios', 'ip': '192.168.0.1', 'username': username, 'password': password, 'secret': password}, #Example Entry
    # Add as many devices as you need
]

for device in devices:
    remove_username(device)

#NOTE: if the username to delete doesn't exist, the script will give an error but if the username exist, the script will run and show proper output

####################################################################################################
