from typing import Callable

norm: Callable[[str],str] = lambda t : t.replace('\n','')

chat_lis = norm('''
div.im_dialogs_scrollable_wrap.nano-content
> ul > li.im_dialog_wrap
''')

chat_name_spans = norm(f'''
{chat_lis}
> a > div.im_dialog_message_wrap
> div > span[my-peer-link="dialogMessage.peerID"]
''')

# sl_chats_name_span = norm(f'''
# {sl_chats_li}
# > a > div.im_dialog_message_wrap
# > div > span[my-peer-link="dialogMessage.peerID"]
# ''')