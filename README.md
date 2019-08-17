The first teverse api wrapper!

There are no docs for this **yet** so you will need to look through the source.

Here is an example:
```PY
import teverse, asyncio
client = teverse.Client()

async def run():
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


loop = asyncio.get_event_loop()
loop.run_until_complete(run())
loop.close()

```