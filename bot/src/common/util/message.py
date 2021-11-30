class MessageUtil:
    @staticmethod
    def new_text_msg(msg: str):
        return {
            'type': 'text',
            'data': {
                'text': msg
            }
        }

    @staticmethod
    def new_at(qq: int):
        return {
            'type': 'at',
            'data': {
                'qq': qq
            }
        }
