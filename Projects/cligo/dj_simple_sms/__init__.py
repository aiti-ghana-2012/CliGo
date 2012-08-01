import urls
import models


def sample_sms_handler(sms):
    print sms.to_message()
