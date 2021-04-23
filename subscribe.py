import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError


def subscriber(payload):
    mailchimp = MailchimpMarketing.Client()
    mailchimp.set_config({
    "api_key": payload['API_KEY'],
    "server": payload['SERVER_PREFIX']
    })

    list_id = payload['LIST_ID']

    member_info = {
        "email_address": payload['SUB_EMAIL'],
        "status": "subscribed"
    }

    try:
        response = mailchimp.lists.add_list_member(list_id, member_info)
        print("response: {}".format(response))
    except ApiClientError as error:
        print("An exception occurred: {}".format(error.text))
