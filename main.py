import os

from praw import Reddit


if __name__ == '__main__':

    client_id = os.environ.get('REDDIT_CLIENT_ID')
    client_secret = os.environ.get('REDDIT_CLIENT_SECRET')
    username = os.environ.get('REDDIT_USERNAME')
    password = os.environ.get('REDDIT_PASSWORD')

    client = Reddit(client_id=client_id,
                    client_secret=client_secret,
                    username=username,
                    password=password,
                    user_agent='Test v1.2.3')

    me = client.user.me()

    # Iterate over comments, edit the comment, and delete it.
    comment_counter = 0
    comments = me.stream.comments(pause_after=1)
    for comment in comments:
        if not comment:
            break
        comment.edit('edited')
        comment.delete()
        comment_counter += 1

        if comment_counter:
            print(f'{comment_counter} comments deleted.', end='\r')
        else:
            print(f'{comment_counter} comments deleted.')

    # Iterate over submission, edit if it's self, and delete it.
    submission_counter = 0
    submissions = me.stream.submissions(pause_after=1)
    for submission in submissions:
        if not submission:
            break
        if submission.is_self:
            submission.edit('edited')
        submission.delete()
        submission_counter += 1

        if submission_counter:
            print(f'{submission_counter} submissions deleted.', end='\r')
        else:
            print(f'{submission_counter} submissions deleted.')
