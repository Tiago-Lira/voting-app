
if __name__ == '__main__':
    from voting.application import manager
    from voting.commands import *  # noqa
    manager.run()
