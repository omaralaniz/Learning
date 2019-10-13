### What is FHS?
_F.H.S - Filesystem Hierarchy Standard_

 #### Directory Structure:



| Directory | Description                                                  |
| --------- | ------------------------------------------------------------ |
| /         | this signifies the root of the directory                     |
| /bin      | the necessary command binaries that need to be accessed by the user |
| /boot     | boot loader files are located in this directory              |
| /dev      | device files<br />devices files are meant for a way for applications to talk to device drivers |
| /etc      | Host specific system wide configuration files <br />popular belief is that this directory may not have for <br />binary files. Configuration text files |
| /home     | this is where the user saves files, and configurations       |
| /lib      | libraries that essential to the /bin and /sbin directories   |
| /media    | mounting points for removable media                          |
| /mnt      | temporarily mounted filesystems<br />mounting:<br />when the OS creates files and directories to a storage system |
| /opt      | Optional application software packages (you should put extra apps HERE) |
| /proc     | virtual filesystem providing kernel and process information. Done automatically by the system |
| /root     | the home directory for root user                             |
| /run      | info about the system since the last boot (for example currently logged in users and daemons). These files must be removed or truncated at the boot |
| /srv      | site specific date served by the system. Such as data and scripts from web servers <br />and data given by FTP. Repos for version control systems |
| /sys      | information about devices, kernel, and driver                |
| /tmp      | temporary files usually removed by the next reboot           |
| /usr      | Secondary Hierarchy for read-only user data and <br />contains the majority of user utilities and applications |
| /var      | files (variable files) whose content is expected to change during the runtime<br />of the system. such as logs and temp e-mail files |

