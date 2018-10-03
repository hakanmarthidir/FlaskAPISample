import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SqlAlchemyTrackModifications = False
    ConnectionString = 'postgresql://postgres:123@localhost/school' or ''
    RedisHost = ''
    RedisAccessKey = ''
    MailPort = 465
    MailServer = 'smtp.gmail.com'
    MailUseTls = False
    MailUseSsl = True
    MailUserName = 'GmailAddress@gmail.com'
    MailUserPass = 'AccountPassword'

