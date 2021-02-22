from azure.devops.connection import Connection
from azure.devops.v6_0.pipelines import PipelinesClient
from msrest.authentication import BasicAuthentication
import config
import menu
from termcolor import colored, cprint

# Fill in with your personal access token and org URL
personal_access_token = config.CLIENT['personal_access_token']
organization_url = config.PROJECT['organization_url']

# Create a connection to the org
credentials = BasicAuthentication('', personal_access_token)
connection = Connection(base_url=organization_url, creds=credentials)

def getBuildList():
    getRunningBuildList()
    menu.getInput('')
    menu.show()

def getRunningBuildList():
    build_client = connection.clients_v6_0.get_build_client()
    get_builds_response = build_client.get_builds(config.PROJECT['name'], status_filter = 'inProgress', query_order = 'startTimeDescending')
    #print(get_builds_response)

    if len(get_builds_response) > 0:
        menu.clear()
        print(colored('Running builds\n', 'cyan', attrs=['reverse', 'bold']))
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
        text += build.trigger_info['pr.sender.name']
    else:
        text += menu.buildBox(str(build.id), ' ' + build.repository.id)
        text += colored(' started by ', 'yellow')
        text += build.requested_by.display_name
    
    text += ' (' + colored(build.definition.name, 'white', attrs=['reverse']) + ')'

    return text


def getSpecificBuildResult(buildId):
    build_client = connection.clients_v6_0.get_build_client()
    get_build_response = build_client.get_build(config.PROJECT['name'], buildId)
    return get_build_response.result
        
    # for pipeline in get_pipeline_response.value:
    #     print(pipeline)

#getBuildList()
#connection = Connection(base_url=organization_url, creds=credentials)

# Get a client (the "core" client provides access to projects, teams, etc)
#core_client = connection.clients.get_core_client()

# Get the first page of projects
# get_projects_response = core_client.get_projects()
# index = 0
# while get_projects_response is not None:
#     for project in get_projects_response.value:
#         pprint.pprint("[" + str(index) + "] " + project.name)
#         index += 1
#     if get_projects_response.continuation_token is not None and get_projects_response.continuation_token != "":
#         # Get the next page of projects
#         get_projects_response = core_client.get_projects(continuation_token=get_projects_response.continuation_token)
#     else:
#         # All projects have been retrieved
#         get_projects_response = None