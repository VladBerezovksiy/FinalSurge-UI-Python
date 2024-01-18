from selenium.webdriver.common.by import By


class MailBoxGeneralPageLocators:
    no_messages_text = (By.XPATH, "//p[text()=\"You have no messages in your Inbox.\"]")


class InboxPageLocators:
    inbox_tab = (By.XPATH, "//a[@href=\"Mailbox\"]")


class SentPageLocators:
    sent_tab = (By.XPATH, "//a[@href=\"Mailbox?sent=1\"]")
