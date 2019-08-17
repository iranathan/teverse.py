The first teverse api wrapper!

There are no docs for this **yet** so you will need to look through the source.

Here is an example:
```PY
import teverse, asyncio
client = teverse.Client()

def run():
    user = await client.User.get_user_by_id('zME5M')
    print(user) # Output:
    '''
       {
            "id":"zME5M",
            "username":"Jay",
            "beta":true,
            "joinTimestamp":"2017-11-23T17:55:06+00:00",
            "games":5
        }
    '''


asyncio.run(run())

```