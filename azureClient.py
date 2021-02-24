from azure.devops.connection import Connection
from azure.devops.v6_0.pipelines import PipelinesClient
from msrest.authentication import BasicAuthentication
from termcolor import colored, cprint
from datetime import date
from datetime import timedelta
import config
import menu
from build_result import build_result

personal_access_token = config.CLIENT['personal_access_token']
organization_url = config.PROJECT['organization_url']

credentials = BasicAuthentication('', personal_access_token)
connection = Connection(base_url=organization_url, creds=credentials)

def getBuildList():
    getRunningBuildList()
    menu.getInput('')
    menu.show()

def getRunningBuildList():
    build_client = connection.clients_v6_0.get_build_client()
    get_builds_response = build_client.get_builds(config.PROJECT['name'], status_filter = 'inProgress', query_order = 'startTimeDescending')

    if len(get_builds_response) > 0:
        menu.clear()
        cprint('Running builds\n', 'cyan', attrs=['reverse', 'bold'])
        for build in get_builds_response:
            buildText = getBuildDetailsText(build)
            if buildText != None:
                print(getBuildDetailsText(build))
                
    else:
        print(colored('No build running...', 'yellow', attrs=['bold']))

def getBuildDetailsText(build):
    text = ''

    if build.reason == 'individualCI':
        return None

    if len(build.trigger_info) and 'pr.title' in build.trigger_info:
        text += menu.buildBox(str(build.id), ' ' + build.trigger_info['pr.title'])
        text += colored(' batched for ', 'yellow')
        text += colored(build.trigger_info['pr.sender.name'], 'cyan')
    else:
        text += menu.buildBox(str(build.id), ' ' + build.repository.id)
        text += colored(' started by ', 'yellow')
        text += colored(build.requested_by.display_name, 'cyan')
    
    text += ' (' + colored(build.definition.name, 'white', attrs=['reverse']) + ')'

    return text


def getSpecificBuildResult(buildId):
    build_client = connection.clients_v6_0.get_build_client()
    get_build_response = build_client.get_build(config.PROJECT['name'], buildId)
    result = build_result(get_build_response.start_time, get_build_response.result)
    return result