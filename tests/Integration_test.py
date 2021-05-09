import pytest,datetime,dotenv,json
from unittest.mock import patch,Mock
from pathlib import Path

from todo_app.app import ViewModel, Lists, create_app
from todo_app.trello_requests import get_BoardId,find_list,get_List,get_Items,add_Item,get_Item,set_Item

@pytest.fixture
def mock_request():
    with patch('requests.request') as mock_get:
        mock_get.side_effect = mock_get_lists
        yield mock_get

@pytest.fixture
def client():
    # Use our test integration config instead of the 'real' version
    file_path = dotenv.find_dotenv('.env.test')
    dotenv.load_dotenv(file_path, override=True)
    # Create the new app.
    test_app = create_app()
    # Use the app to create a test_client that can be used in our tests.
    with test_app.test_client() as client:
        yield client

def test_index_page(mock_request,client):
    response = client.get('/')

def mock_get_lists(http_method,url,params,headers):
    if url == f'https://api.trello.com/1/boards/603b8faf893153146df47462/lists':
        response = Mock()
        # sample_trello_lists_response should point to some test response data
        json_payload = '[{"id":"603b8faf893153146df47463","name":"To Do","closed":false,"pos":16384,"softLimit":null,"idBoard":"603b8faf893153146df47462","subscribed":false},{"id":"603b8faf893153146df47464","name":"Doing","closed":false,"pos":32768,"softLimit":null,"idBoard":"603b8faf893153146df47462","subscribed":false},{"id":"603b8faf893153146df47465","name":"Done","closed":false,"pos":49152,"softLimit":null,"idBoard":"603b8faf893153146df47462","subscribed":false}]'
        response.json.return_value = json.loads(json_payload)
        return response
    
    if url == f'https://api.trello.com/1/members/me/boards':
        response = Mock()
        json_payload = '[{"name":"SqmIler01","desc":"","descData":null,"closed":false,"dateClosed":null,"idOrganization":"603b8b1b4f14c66e4eb6f86e","idEnterprise":null,"limits":null,"pinned":null,"shortLink":"6YqdMuoc","powerUps":[],"dateLastActivity":"2021-04-13T10:20:28.795Z","idTags":[],"datePluginDisable":null,"creationMethod":"automatic","ixUpdate":null,"enterpriseOwned":false,"idBoardSource":null,"idMemberCreator":"603b8b0570d61831289b3ec3","id":"603b8faf893153146df47462","starred":false,"url":"https://trello.com/b/6YqdMuoc/sqmiler01"}]'
        response.json.return_value = json.loads(json_payload)
        return response

    #To Do
    if url == f'https://api.trello.com/1/lists/603b8faf893153146df47463/cards':
        response = Mock()
        json_payload = '[{"id":"603b8fd8acd0617a9083538c","checkItemStates":null,"closed":false,"dateLastActivity":"2021-04-05T14:41:54.021Z","desc":"Git","descData":{"emoji":{}},"dueReminder":null,"idBoard":"603b8faf893153146df47462","idList":"603b8faf893153146df47463","idMembersVoted":[],"idShort":3,"idAttachmentCover":null,"idLabels":[],"manualCoverAttachment":false,"name":"Module 01","pos":65535,"shortLink":"JxpPj9Pj","isTemplate":false,"cardRole":null,"badges":{"attachmentsByType":{"trello":{"board":0,"card":0}},"location":false,"votes":0,"viewingMemberVoted":false,"subscribed":false,"fogbugz":"","checkItems":0,"checkItemsChecked":0,"checkItemsEarliestDue":null,"comments":0,"attachments":0,"description":true,"due":null,"dueComplete":false,"start":null},"dueComplete":false,"due":null,"idChecklists":[],"idMembers":[],"labels":[],"shortUrl":"https://trello.com/c/JxpPj9Pj","start":null,"subscribed":false,"url":"https://trello.com/c/JxpPj9Pj/3-module-01","cover":{"idAttachment":null,"color":null,"idUploadedBackground":null,"size":"normal","brightness":"light","idPlugin":null}},{"id":"603b8fbe7e6f76736df8f830","checkItemStates":null,"closed":false,"dateLastActivity":"2021-03-06T16:14:33.349Z","desc":"get new brake pads for CB1000","descData":{"emoji":{}},"dueReminder":null,"idBoard":"603b8faf893153146df47462","idList":"603b8faf893153146df47463","idMembersVoted":[],"idShort":1,"idAttachmentCover":null,"idLabels":[],"manualCoverAttachment":false,"name":"Change brake pads","pos":65535.5,"shortLink":"ccSJGSrO","isTemplate":false,"cardRole":null,"badges":{"attachmentsByType":{"trello":{"board":0,"card":0}},"location":false,"votes":0,"viewingMemberVoted":false,"subscribed":false,"fogbugz":"","checkItems":0,"checkItemsChecked":0,"checkItemsEarliestDue":null,"comments":0,"attachments":0,"description":true,"due":null,"dueComplete":false,"start":null},"dueComplete":false,"due":null,"idChecklists":[],"idMembers":[],"labels":[],"shortUrl":"https://trello.com/c/ccSJGSrO","start":null,"subscribed":false,"url":"https://trello.com/c/ccSJGSrO/1-change-brake-pads","cover":{"idAttachment":null,"color":null,"idUploadedBackground":null,"size":"normal","brightness":"light","idPlugin":null}},{"id":"603e9f548b53f039972e63a3","checkItemStates":null,"closed":false,"dateLastActivity":"2021-04-05T11:56:13.676Z","desc":"paddsssss","descData":{"emoji":{}},"dueReminder":null,"idBoard":"603b8faf893153146df47462","idList":"603b8faf893153146df47463","idMembersVoted":[],"idShort":9,"idAttachmentCover":null,"idLabels":[],"manualCoverAttachment":false,"name":"Brake pads","pos":147455,"shortLink":"YisntaIc","isTemplate":false,"cardRole":null,"badges":{"attachmentsByType":{"trello":{"board":0,"card":0}},"location":false,"votes":0,"viewingMemberVoted":false,"subscribed":false,"fogbugz":"","checkItems":0,"checkItemsChecked":0,"checkItemsEarliestDue":null,"comments":0,"attachments":0,"description":true,"due":null,"dueComplete":false,"start":null},"dueComplete":false,"due":null,"idChecklists":[],"idMembers":[],"labels":[],"shortUrl":"https://trello.com/c/YisntaIc","start":null,"subscribed":false,"url":"https://trello.com/c/YisntaIc/9-brake-pads","cover":{"idAttachment":null,"color":null,"idUploadedBackground":null,"size":"normal","brightness":"light","idPlugin":null}},{"id":"6044bd4d6bc3d662c5ab5b0e","checkItemStates":null,"closed":false,"dateLastActivity":"2021-04-12T10:26:24.063Z","desc":"OOP222","descData":{"emoji":{}},"dueReminder":null,"idBoard":"603b8faf893153146df47462","idList":"603b8faf893153146df47463","idMembersVoted":[],"idShort":11,"idAttachmentCover":null,"idLabels":[],"manualCoverAttachment":false,"name":"Module 02","pos":180223,"shortLink":"yRKnfRCA","isTemplate":false,"cardRole":null,"badges":{"attachmentsByType":{"trello":{"board":0,"card":0}},"location":false,"votes":0,"viewingMemberVoted":false,"subscribed":false,"fogbugz":"","checkItems":0,"checkItemsChecked":0,"checkItemsEarliestDue":null,"comments":0,"attachments":0,"description":true,"due":null,"dueComplete":false,"start":null},"dueComplete":false,"due":null,"idChecklists":[],"idMembers":[],"labels":[],"shortUrl":"https://trello.com/c/yRKnfRCA","start":null,"subscribed":false,"url":"https://trello.com/c/yRKnfRCA/11-module-02","cover":{"idAttachment":null,"color":null,"idUploadedBackground":null,"size":"normal","brightness":"light","idPlugin":null}},{"id":"60576ca1df6032852aed5d61","checkItemStates":null,"closed":false,"dateLastActivity":"2021-03-30T15:18:09.706Z","desc":"paddsssss","descData":null,"dueReminder":null,"idBoard":"603b8faf893153146df47462","idList":"603b8faf893153146df47463","idMembersVoted":[],"idShort":15,"idAttachmentCover":null,"idLabels":[],"manualCoverAttachment":false,"name":"Brake pads","pos":204799,"shortLink":"eghsMw6I","isTemplate":false,"cardRole":null,"badges":{"attachmentsByType":{"trello":{"board":0,"card":0}},"location":false,"votes":0,"viewingMemberVoted":false,"subscribed":false,"fogbugz":"","checkItems":0,"checkItemsChecked":0,"checkItemsEarliestDue":null,"comments":0,"attachments":0,"description":true,"due":null,"dueComplete":false,"start":null},"dueComplete":false,"due":null,"idChecklists":[],"idMembers":[],"labels":[],"shortUrl":"https://trello.com/c/eghsMw6I","start":null,"subscribed":false,"url":"https://trello.com/c/eghsMw6I/15-brake-pads","cover":{"idAttachment":null,"color":null,"idUploadedBackground":null,"size":"normal","brightness":"light","idPlugin":null}},{"id":"605762b1d59617719de31129","checkItemStates":null,"closed":false,"dateLastActivity":"2021-03-21T15:21:35.210Z","desc":"In Little China","descData":{"emoji":{}},"dueReminder":null,"idBoard":"603b8faf893153146df47462","idList":"603b8faf893153146df47463","idMembersVoted":[],"idShort":14,"idAttachmentCover":null,"idLabels":[],"manualCoverAttachment":false,"name":"Trouble","pos":212991,"shortLink":"3BQdlV0X","isTemplate":false,"cardRole":null,"badges":{"attachmentsByType":{"trello":{"board":0,"card":0}},"location":false,"votes":0,"viewingMemberVoted":false,"subscribed":false,"fogbugz":"","checkItems":0,"checkItemsChecked":0,"checkItemsEarliestDue":null,"comments":0,"attachments":0,"description":true,"due":null,"dueComplete":false,"start":null},"dueComplete":false,"due":null,"idChecklists":[],"idMembers":[],"labels":[],"shortUrl":"https://trello.com/c/3BQdlV0X","start":null,"subscribed":false,"url":"https://trello.com/c/3BQdlV0X/14-trouble","cover":{"idAttachment":null,"color":null,"idUploadedBackground":null,"size":"normal","brightness":"light","idPlugin":null}}]'
        response.json.return_value = json.loads(json_payload)
        return response
    
    #Doing
    if url == f'https://api.trello.com/1/lists/603b8faf893153146df47464/cards':
        response = Mock()
        json_payload = '[{"id":"6057626a5bcbda0de54a84aa","checkItemStates":null,"closed":false,"dateLastActivity":"2021-04-10T15:08:32.682Z","desc":"In Little China","descData":{"emoji":{}},"dueReminder":null,"idBoard":"603b8faf893153146df47462","idList":"603b8faf893153146df47464","idMembersVoted":[],"idShort":13,"idAttachmentCover":null,"idLabels":[],"manualCoverAttachment":false,"name":"Big Trouble","pos":221183.5,"shortLink":"PY5NlzQj","isTemplate":false,"cardRole":null,"badges":{"attachmentsByType":{"trello":{"board":0,"card":0}},"location":false,"votes":0,"viewingMemberVoted":false,"subscribed":false,"fogbugz":"","checkItems":0,"checkItemsChecked":0,"checkItemsEarliestDue":null,"comments":0,"attachments":0,"description":true,"due":null,"dueComplete":false,"start":null},"dueComplete":false,"due":null,"idChecklists":[],"idMembers":[],"labels":[],"shortUrl":"https://trello.com/c/PY5NlzQj","start":null,"subscribed":false,"url":"https://trello.com/c/PY5NlzQj/13-big-trouble","cover":{"idAttachment":null,"color":null,"idUploadedBackground":null,"size":"normal","brightness":"light","idPlugin":null}}]'
        response.json.return_value = json.loads(json_payload)
        return response

    #Done
    if url == f'https://api.trello.com/1/lists/603b8faf893153146df47465/cards':
        response = Mock()
        json_payload = '[{"id":"60577dc059f0e757ef88adea","checkItemStates":null,"closed":false,"dateLastActivity":"2021-04-10T14:49:58.395Z","desc":"In Little China","descData":{"emoji":{}},"dueReminder":null,"idBoard":"603b8faf893153146df47462","idList":"603b8faf893153146df47465","idMembersVoted":[],"idShort":22,"idAttachmentCover":null,"idLabels":[],"manualCoverAttachment":false,"name":"Trouble2","pos":835583,"shortLink":"uu6V2M88","isTemplate":false,"cardRole":null,"badges":{"attachmentsByType":{"trello":{"board":0,"card":0}},"location":false,"votes":0,"viewingMemberVoted":false,"subscribed":false,"fogbugz":"","checkItems":0,"checkItemsChecked":0,"checkItemsEarliestDue":null,"comments":0,"attachments":0,"description":true,"due":null,"dueComplete":false,"start":null},"dueComplete":false,"due":null,"idChecklists":[],"idMembers":[],"labels":[],"shortUrl":"https://trello.com/c/uu6V2M88","start":null,"subscribed":false,"url":"https://trello.com/c/uu6V2M88/22-trouble2","cover":{"idAttachment":null,"color":null,"idUploadedBackground":null,"size":"normal","brightness":"light","idPlugin":null}},{"id":"60576cbf71386d2f67265eba","checkItemStates":null,"closed":false,"dateLastActivity":"2021-04-10T14:49:59.640Z","desc":"In Little China","descData":{"emoji":{}},"dueReminder":null,"idBoard":"603b8faf893153146df47462","idList":"603b8faf893153146df47465","idMembersVoted":[],"idShort":16,"idAttachmentCover":null,"idLabels":[],"manualCoverAttachment":false,"name":"Brake pads","pos":901119,"shortLink":"03zVPMJ7","isTemplate":false,"cardRole":null,"badges":{"attachmentsByType":{"trello":{"board":0,"card":0}},"location":false,"votes":0,"viewingMemberVoted":false,"subscribed":false,"fogbugz":"","checkItems":0,"checkItemsChecked":0,"checkItemsEarliestDue":null,"comments":0,"attachments":0,"description":true,"due":null,"dueComplete":false,"start":null},"dueComplete":false,"due":null,"idChecklists":[],"idMembers":[],"labels":[],"shortUrl":"https://trello.com/c/03zVPMJ7","start":null,"subscribed":false,"url":"https://trello.com/c/03zVPMJ7/16-brake-pads","cover":{"idAttachment":null,"color":null,"idUploadedBackground":null,"size":"normal","brightness":"light","idPlugin":null}},{"id":"603b8fe3a9fd0418a86ffa17","checkItemStates":null,"closed":false,"dateLastActivity":"2021-04-10T14:50:00.676Z","desc":"Potatoes","descData":{"emoji":{}},"dueReminder":null,"idBoard":"603b8faf893153146df47462","idList":"603b8faf893153146df47465","idMembersVoted":[],"idShort":4,"idAttachmentCover":null,"idLabels":[],"manualCoverAttachment":false,"name":"Cook dinner","pos":966655,"shortLink":"EXmOY5M0","isTemplate":false,"cardRole":null,"badges":{"attachmentsByType":{"trello":{"board":0,"card":0}},"location":false,"votes":0,"viewingMemberVoted":false,"subscribed":false,"fogbugz":"","checkItems":0,"checkItemsChecked":0,"checkItemsEarliestDue":null,"comments":0,"attachments":0,"description":true,"due":null,"dueComplete":false,"start":null},"dueComplete":false,"due":null,"idChecklists":[],"idMembers":[],"labels":[],"shortUrl":"https://trello.com/c/EXmOY5M0","start":null,"subscribed":false,"url":"https://trello.com/c/EXmOY5M0/4-cook-dinner","cover":{"idAttachment":null,"color":null,"idUploadedBackground":null,"size":"normal","brightness":"light","idPlugin":null}},{"id":"60572d8872b1027870438a58","checkItemStates":null,"closed":false,"dateLastActivity":"2021-04-10T14:50:02.644Z","desc":"need more space","descData":{"emoji":{}},"dueReminder":null,"idBoard":"603b8faf893153146df47462","idList":"603b8faf893153146df47465","idMembersVoted":[],"idShort":12,"idAttachmentCover":null,"idLabels":[],"manualCoverAttachment":false,"name":"Clear garage","pos":1032191,"shortLink":"4Hx7A3eh","isTemplate":false,"cardRole":null,"badges":{"attachmentsByType":{"trello":{"board":0,"card":0}},"location":false,"votes":0,"viewingMemberVoted":false,"subscribed":false,"fogbugz":"","checkItems":0,"checkItemsChecked":0,"checkItemsEarliestDue":null,"comments":0,"attachments":0,"description":true,"due":null,"dueComplete":false,"start":null},"dueComplete":false,"due":null,"idChecklists":[],"idMembers":[],"labels":[],"shortUrl":"https://trello.com/c/4Hx7A3eh","start":null,"subscribed":false,"url":"https://trello.com/c/4Hx7A3eh/12-clear-garage","cover":{"idAttachment":null,"color":null,"idUploadedBackground":null,"size":"normal","brightness":"light","idPlugin":null}},{"id":"6059cfce7cd9c04d7550d812","checkItemStates":null,"closed":false,"dateLastActivity":"2021-04-13T10:20:25.749Z","desc":"Find a new gardener","descData":{"emoji":{}},"dueReminder":null,"idBoard":"603b8faf893153146df47462","idList":"603b8faf893153146df47465","idMembersVoted":[],"idShort":23,"idAttachmentCover":null,"idLabels":[],"manualCoverAttachment":false,"name":"Gardener","pos":1097727,"shortLink":"2RROo7G0","isTemplate":false,"cardRole":null,"badges":{"attachmentsByType":{"trello":{"board":0,"card":0}},"location":false,"votes":0,"viewingMemberVoted":false,"subscribed":false,"fogbugz":"","checkItems":0,"checkItemsChecked":0,"checkItemsEarliestDue":null,"comments":0,"attachments":0,"description":true,"due":null,"dueComplete":false,"start":null},"dueComplete":false,"due":null,"idChecklists":[],"idMembers":[],"labels":[],"shortUrl":"https://trello.com/c/2RROo7G0","start":null,"subscribed":false,"url":"https://trello.com/c/2RROo7G0/23-gardener","cover":{"idAttachment":null,"color":null,"idUploadedBackground":null,"size":"normal","brightness":"light","idPlugin":null}},{"id":"60576cc956ef550de6ca474d","checkItemStates":null,"closed":false,"dateLastActivity":"2021-04-13T10:20:27.307Z","desc":"In Little China Episode 2","descData":{"emoji":{}},"dueReminder":null,"idBoard":"603b8faf893153146df47462","idList":"603b8faf893153146df47465","idMembersVoted":[],"idShort":17,"idAttachmentCover":null,"idLabels":[],"manualCoverAttachment":false,"name":"Trouble","pos":1163263,"shortLink":"ZZD5GTwn","isTemplate":false,"cardRole":null,"badges":{"attachmentsByType":{"trello":{"board":0,"card":0}},"location":false,"votes":0,"viewingMemberVoted":false,"subscribed":false,"fogbugz":"","checkItems":0,"checkItemsChecked":0,"checkItemsEarliestDue":null,"comments":0,"attachments":0,"description":true,"due":null,"dueComplete":false,"start":null},"dueComplete":false,"due":null,"idChecklists":[],"idMembers":[],"labels":[],"shortUrl":"https://trello.com/c/ZZD5GTwn","start":null,"subscribed":false,"url":"https://trello.com/c/ZZD5GTwn/17-trouble","cover":{"idAttachment":null,"color":null,"idUploadedBackground":null,"size":"normal","brightness":"light","idPlugin":null}},{"id":"603ea5b07265cf7c26409360","checkItemStates":null,"closed":false,"dateLastActivity":"2021-04-13T10:20:28.795Z","desc":"new module","descData":{"emoji":{}},"dueReminder":null,"idBoard":"603b8faf893153146df47462","idList":"603b8faf893153146df47465","idMembersVoted":[],"idShort":10,"idAttachmentCover":null,"idLabels":[],"manualCoverAttachment":false,"name":"Module 03","pos":1228799,"shortLink":"CCakIMSj","isTemplate":false,"cardRole":null,"badges":{"attachmentsByType":{"trello":{"board":0,"card":0}},"location":false,"votes":0,"viewingMemberVoted":false,"subscribed":false,"fogbugz":"","checkItems":0,"checkItemsChecked":0,"checkItemsEarliestDue":null,"comments":0,"attachments":0,"description":true,"due":null,"dueComplete":false,"start":null},"dueComplete":false,"due":null,"idChecklists":[],"idMembers":[],"labels":[],"shortUrl":"https://trello.com/c/CCakIMSj","start":null,"subscribed":false,"url":"https://trello.com/c/CCakIMSj/10-module-03","cover":{"idAttachment":null,"color":null,"idUploadedBackground":null,"size":"normal","brightness":"light","idPlugin":null}}]'
        response.json.return_value = json.loads(json_payload)
        return response 

    return None

def mock_edit_item(http_method,url,params,headers):
    if url == f'https://api.trello.com/1/cards/603b8fd8acd0617a9083538c':
        response = Mock()
        # sample_trello_lists_response should point to some test response data
        test_items = {
            "dateLastActivity": "2021-04-05T14:41:54.021Z",
            "desc": "Git",
            "name": "Module 01",
            "idList":"603b8faf893153146df47463"}
        #json_payload = '{"id":"603b8fd8acd0617a9083538c","checkItemStates":[],"closed":false,"dateLastActivity":"2021-04-05T14:41:54.021Z","desc":"Git","descData":{"emoji":{}},"dueReminder":null,"idBoard":"603b8faf893153146df47462","idList":"603b8faf893153146df47463","idMembersVoted":[],"idShort":3,"idAttachmentCover":null,"idLabels":[],"manualCoverAttachment":false,"name":"Module 01","pos":65535,"shortLink":"JxpPj9Pj","isTemplate":false,"cardRole":null,"dueComplete":false,"due":null,"email":null,"labels":[],"shortUrl":"https://trello.com/c/JxpPj9Pj","start":null,"url":"https://trello.com/c/JxpPj9Pj/3-module-01","idMembers":[],"idChecklists":[],"badges":{"attachmentsByType":{"trello":{"board":0,"card":0}},"location":false,"votes":0,"viewingMemberVoted":false,"subscribed":false,"fogbugz":"","checkItems":0,"checkItemsChecked":0,"checkItemsEarliestDue":null,"comments":0,"attachments":0,"description":true,"due":null,"dueComplete":false,"start":null},"subscribed":false,"cover":{"idAttachment":null,"color":null,"idUploadedBackground":null,"size":"normal","brightness":"light","idPlugin":null}}'
        response.json.return_value = test_items
        return response
    
    if 'https://api.trello.com/1/lists/' in url:
        response = Mock()
        # sample_trello_lists_response should point to some test response data
        json_payload = '{"id":"603b8faf893153146df47463","name":"To Do","closed":false,"pos":16384,"idBoard":"603b8faf893153146df47462"}'
        response.json.return_value = json.loads(json_payload)
        return response

    if url == f'https://api.trello.com/1/members/me/boards':
        response = Mock()
        json_payload = [
            {"name":"SqmIler01",
            "desc":"",
            "descData":None,
            "dateLastActivity":"2021-04-13T10:20:28.795Z",
            "id":"603b8faf893153146df47462",
            "url":"https://trello.com/b/6YqdMuoc/sqmiler01"}
            ]
        response.json.return_value = json_payload #json.loads(json_payload)
        return response

    if url == f'https://api.trello.com/1/boards/603b8faf893153146df47462/lists':
        response = Mock()
        json_payload = [
            {
                "id":"603b8faf893153146df47463",
                "name":"To Do",
                "idBoard":"603b8faf893153146df47462"},
            {
                "id":"603b8faf893153146df47464",
                "name":"Doing",
                "idBoard":"603b8faf893153146df47462"},
            {
                "id":"603b8faf893153146df47465",
                "name":"Done",
                "idBoard":"603b8faf893153146df47462"}
            ]
        response.json.return_value = json_payload #json.loads(json_payload)
        return response
def test_editItem_page(mock_request,client):
    # Replace call to requests.get(url) with our own function
    mock_request.side_effect = mock_edit_item 
    #response = client.request('/')
    response = client.get('/EditItem.html?id=603b8fd8acd0617a9083538c')

