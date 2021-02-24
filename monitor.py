import time
from termcolor import colored
import notifications
import azureClient
import config
import menu

def notifyMeWhenBuildIsFinish(buildNumbers):
    running_builds = buildNumbers.split(',')

    while len(running_builds) > 0:
        for build_to_monitor in running_builds:            
            build_result = azureClient.getSpecificBuildResult(build_to_monitor)
            print('checking build ' + colored(build_to_monitor, 'cyan') + ' Running for ' + colored(str(build_result.get_running_time()), 'yellow') + ' minutes')
            if build_result.result != None:
                sendResultNotification(build_to_monitor, build_result)
                running_builds.remove(build_to_monitor)
        time.sleep(config.MONITORING['check_interval_seconds'])
    menu.show('All your builds are done...')


def sendResultNotification(buildNumber, result):
    notifications.notify('Build #' + buildNumber + ' [' + result.result + ']', result.get_result_text())