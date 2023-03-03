import subprocess
import os
import minecraft_launcher_lib
import sys
print("Insert your Minecraft Username")


options = {
    "username": input(),
    
}

print ("Insert version type (optifine/vanilla/optipvp/fabric)")

version = input()

if version == "fabric":
    latest_version = "fabric-loader-" +minecraft_launcher_lib.fabric.get_latest_loader_version() +"-1.19.3"
    minecraft_directory = minecraft_launcher_lib.utils.get_minecraft_directory()
    minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(latest_version, minecraft_directory, options)
    subprocess.call(minecraft_command)
if version == "optifine":
    latest_version = "1.19.3-OptiFine_HD_U_I2_pre5"
    minecraft_directory = minecraft_launcher_lib.utils.get_minecraft_directory()
    minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(latest_version, minecraft_directory, options)
    subprocess.call(minecraft_command)
if version == "optipvp":
    latest_version = "OptiPvP"
    minecraft_directory = minecraft_launcher_lib.utils.get_minecraft_directory()
    minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(latest_version, minecraft_directory, options)
    subprocess.call(minecraft_command)
if version == "vanilla":
    latest_version = "1.19.3"
    minecraft_directory = minecraft_launcher_lib.utils.get_minecraft_directory()
    minecraft_launcher_lib.install.install_minecraft_version(latest_version, minecraft_directory)
    minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(latest_version, minecraft_directory, options)
    subprocess.call(minecraft_command)
if version == "custom":
    print("If you have a custom minecraft version downloaded, please spell exactly its name and it will start!")
    latest_version = input()
    minecraft_directory = minecraft_launcher_lib.utils.get_minecraft_directory()
    minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(latest_version, minecraft_directory, options)
    subprocess.call(minecraft_command)
    
