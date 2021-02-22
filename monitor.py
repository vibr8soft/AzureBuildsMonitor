import time
import notifications
import azureClient
import config
import menu

def notifyMeWhenBuildIsFinish(buildNumbers):
    running_builds = buildNumbers.split(',')

    while len(running_builds) > 0:
        for build_to_monitor in running_builds:
            print('checking build ' + build_to_monitor + '...')
            build_result = azureClient.getSpecificBuildResult(build_to_monitor)
            if build_result != None:
                sendResultNotification(build_to_monitor, build_result)
                running_builds.remove(build_to_monitor)
        time.sleep(config.MONITORING['check_interval_seconds'])
    menu.show('All your builds are done...')


def sendResultNotification(buildNumber, result):
    text = ''

    if result == 'succeeded': 
        text = 'Congrats mate! Your build as succeeded! Your mom must be proud!'
    elif result == 'canceled':    
        text = 'oH shoots! Someone cancelled your build!'
    elif result == 'failed':
        text = 'Darn the heck! Everybody fail the first time!!'
    elif result == 'partiallySucceeded':
        text = 'Part of your build did succeeded... but we are here for the whole shabang!'
    else:
        text = 'Seems like Azure pulled a new result out of its pants...'

    notifications.notify('Build #' + buildNumber + ' [' + result + ']', text)
