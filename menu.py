import sys
import os
from termcolor import colored, cprint
import notifications
import azureClient
import monitor

def show(confirmMessage = None):
    clear()
    print(colored('-= Azure Builds Monitor =-', 'cyan', attrs=['reverse', 'bold']))
    print()

    print(buildChoiceMenu())

    if confirmMessage != None:
        cprint(confirmMessage, 'yellow', attrs=['bold'])

    choice = getInput('Enter selection: ')

    if choice.lower() == "t":
        manageNotificationTest()
    elif choice.lower() == "s":
        manageShowRunningBuilds()
    elif choice.lower() == "m":
        monitoringMenu()
    elif choice.lower() == "q":
        sys.exit
    else:
        show()

def buildChoiceMenu():
    return buildBox('T', 'est notifications\n') + buildBox('M', 'onitor your builds\n') + buildBox('S', 'how active builds\n') + buildBox('Q', 'uit\n')

def buildBox(choice, label):
    return colored('[', 'cyan') + choice + colored(']', 'cyan') +  label

def clear():
    os.system('clear')

def getInput(text):
    return input('\n\n' + text)

#### Menu options ###
def manageNotificationTest():
    notifications.notify("Yo...", "Its a me... mario")
    show('You shall receive a notif or a permission request')

def manageShowRunningBuilds():
    azureClient.getBuildList()

def monitoringMenu():
    cprint('Please enter the list of builds you want to monitor.', 'white', attrs=['bold'])
    cprint('ie: 1234,1432,1243\n', 'white')
    builds = getInput('Builds to monitor: ')
    monitor.notifyMeWhenBuildIsFinish(builds)