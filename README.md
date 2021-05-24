# <b>UsergeAntiSpamApi</b>

- [<b>Installation</b>](#installation)
- [<b>Documentation</b>](#documentation)
- [<b>Examples</b>](#examples)
  - [<b>Authorisation</b>](#authorisation)
  - [<b>Bans</b>](#bans)
  - [<b>Tokens</b>](#tokens)
  - [<b>Version</b>](#version)
  - [<b>Stats</b>](#stats)
- [<b>Copyright</b>](#copyright)

<br>

# <b>Installation</b>

```shell
pip install UsergeAntiSpamApi
```

<br>

# <b>Documentation</b>

You can read our Documention on https://docs.userge.tk

<br>

# <b>Examples</b>

## <b>Authorisation</b>

```python
from UsergeAntiSpamApi import Client

API_KEY = "Your_API_KEY"

client = Client(API_KEY)
```

#### <b>Parameters</b>

Parameter | description
--------- | -----------
`api_key` | Your [API KEY](#getting-your-own-token)

<br>

## <b>Bans</b>

### <b>Getting a specific ban</b>

```python
print(client.getban(777000))
```

#### <b>Parameters</b>

Parameter | description
--------- | -----------
`user_id` | Id of Telegram User.

<br>

### <b>Getting a list of all bans</b>

```python
print(client.getbans())
```

#### <b>Required Permission Level</b>
`Admin`

Read more about Bans from [here](https://docs.userge.tk/#bans)

<br>

## <b>Tokens</b>

### <b>Getting your own token</b>

To get your own token, go to [@UsergeFedBot](https://t.me/UsergeFedBot) and create one.

<br>

### <b>Getting about your own token</b>

```python
print(client.get_me())
```

<br>

### <b>Deleting your own token</b>

```python
client.delete_my_token()
```

Read more about Tokens from [here](https://docs.userge.tk/#tokens)

<br>

## <b>Version</b>

```python
print(client.get_version())
```

<br>

## <b>Stats</b>

```python
print(client.get_api_stats())
```

<br>

# <b>Copyright</b>

Copyright (C) 2021 by UsergeTeam@Github, < https://github.com/UsergeTeam >.

This project is part of < https://github.com/UsergeTeam > project,
and is released under the "GNU v3.0 License Agreement".
Please see < https://github.com/Krishna-Singhal/Userge-Federation/blob/master/LICENSE >

All rights reserved.