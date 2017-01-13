---
layout: post
permalink: /virtualbox_instructions/
---

## Setting up the "UT Biocomputing" virtual machine

The "UT Biocomputing" virtual machine provides users with a basic Ubuntu Linux installation (including bash, Python, R, and git). Minimum requirements for the host machine are as follows:

  + CPU: Any mostly-modern, 64-bit, x86-compatible CPU; if your computer was built/bought after 2009 or so, you should be ok.
  + RAM: 2-GB at the *very* least; 4-GB or more is preferable.
  + Disk: 15-GB at the *very* least; the VM image can grow to 40+ GB, so plan for that if you're using the VM to process data.
  + Host OS: A 64-bit version of Windows or OS X.


1. Download the VirtualBox installer for your platform:
  * **Windows**: http://download.virtualbox.org/virtualbox/5.0.14/VirtualBox-5.0.14-105127-Win.exe
  * **Mac OS X**: http://download.virtualbox.org/virtualbox/5.0.14/VirtualBox-5.0.14-105127-OSX.dmg
1. Install VirtualBox.
  * **Windows**:
    1. Start Explorer and navigate to your "Downloads" folder.
    1. Double-click on the downloaded ".exe" file to start the installation wizard
    1. Follow the instructions in the installation wizard, accepting any defaults when prompted.
  * **Mac OS X**
    1. Start Finder and navigate to your "Downloads" folder
    1. Double-click on the downloaded ".dmg" file, and a "VirtualBox" Finder window will appear.
    1. Double-click on the "VirtualBox.pkg" icon to run installation wizard
    1. Follow the instructions in the installation wizard, accepting any defaults when prompted.
1. Download the VirtualBox Guest Extension pack: https://download.virtualbox.org/virtualbox/5.0.14/Oracle_VM_VirtualBox_Extension_Pack-5.0.14-105127.vbox-extpack
1. Download the UT Biocomputing VirtualBox image: http://download.lab7.io/utbio-linux-vm.ova. **WARNING**: This is a _large_ (~3.2-GB) download!
1. Start VirtualBox.
  * **Windows**: Click on the VirtualBox icon, which can be found in the Start Menu, Desktop, Quick Launch Bar, and/or "Apps" list (Windows 8 or later).
  * **Mac OS X**: Navigate to the "Applications" folder in Finder, and double-click on the "VirtualBox" application icon.
1. Install the VirtualBox Guest Extensions.
  1. From VirtualBox, click on the "File" (Windows) or "VirtualBox" (Mac OS X) menu, and select the "Preferences..." option.
  1. Select the "Extensions" tab in the dialog box that appears.
  1. Click on the "Adds New Package" button (the one with an upside-down triangle).
  1. In the file-selection dialog, navigate to your "Downloads" folder, and double-click on "Oracle_VM_VirtualBox_Extension_Pack-5.0.14-105127.vbox-extpack" file you downloaded in Step 3 above.
  1. Click the "Install" button on the confirmation dialog that appears.
  1. In the EULA (license agreement) dialog, scroll to the bottom, and then click the "I Agree" button.
  1. If prompted, click "Yes" (Windows) or provide your password (Mac OS X) to allow the installer to run with administrator privileges.
  1. Click "OK" to confirm the successful installation of the extension pack.
  1. The "Extensions" tab should now show an "Oracle VM VirtualBox Extension Pack" item with a green check mark in the "Active" column and "5.0.14r105127" in the "Version" column.
1. Import the UT Biocomputing Linux VM. **WARNING**: You will need ~12-GB of free space on your hard drive for the virtual machine (VM) to import correctly and be usable.
  1. From VirtualBox, click on the "File" menu, and select the "Import Appliance..." option.
  1. Click the "Choose a file to import" button (the one with the green up arrow).
  1. In the file-selection dialog, navigate to your "Downloads" folder, and double-lick on the "utbio-linux-vm.ova" file you downloaded in Step 4 above.
  1. Click the "Next" (or "Continue") button.
  1. In the "Appliance settings" dialog, make sure the "Reinitialize the MAC address of all network" option is selected (i.e., checked). **NOTE**: This is **critical**; failing to select this option could cause major network problems when you start the VM (possibly including calls from unhappy IT departments).
  1. Click the "Import" button, and wait for the import process to finish. The import process may take many minutes, depending on the speed of your CPU and hard drive.
  1. If your computer has 2-GB of RAM (or if your computer runs very slowly when the VM is active), decrease the amount memory allocated to the VM. To do this, select the "UT Biocomputing" VM from the VM list and click on the "Settings" button. In the dialog box that appears, click on the "System" tab, and then use the "Base Memory" slider (or text input box) to decrease the VM memory to "512 MB". Click "OK" to confirm the changes to the VM.
  1. Once the VM imports successfully, you can delete the "utbio-linux-vm.ova" file from your "Downloads" folder to save some space.


## Using the "UT Biocomputing" virtual machine

To start the "UT Biocomputing" virtual machine:

  1. From the VirtualBox VM list, select the "UT Biocomputing" VM by clicking on it.
  1. Click on the "Start" button (the big, green right-arrow) to boot the VM.

To shutdown the "UT Biocomputing" virtual machine:

  + Method 1: _Within the VM_, click on the "Start" menu (little mouse icon in the bottom left). Select "Logout" (user icon with a right arrow, at the top of the menu), and then select "Shut Down".
  + Method 2: _Within the VM_, start a command terminal ("Start" -> "Terminal Emulator"). From the bash shell, type `sudo poweroff` and hit &lt;Enter&gt;.

Note that you will want to shutdown the VM.
