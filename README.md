
# mail-tester

A simple python email sender.

this project was made to assist the research part of the IPSENHO course on HSLeiden
and has been made public for documentation purpouses


## Disclaimer

This project should not be used to spam mails to people.

it's sole purpouse is helping test mail deliverability when running a custom mail server (like [Docker mailserver](https://github.com/docker-mailserver/docker-mailserver))


## Usage/Examples

To use this project first rename `.evn.example` to `.env`


and set the variables.
| Variable  | Description                | Required Y/N |
| :-------- | :------------------------- | :------  |
| `SMTP_SERVER` |  The address of the SMTP server used for sending emails | **Yes** |
| `SMTP_PORT` | the port number used to connect to the SMTP server `default: 587` | **Yes** |
| `SMTP_USER` | email address of the sender. | **Yes** |
| `SMTP_PASS` | the password associated with the SMTP user's email account | **Yes** |
| `RECIPIENT` | the email address of the recipient. | **Yes** |
| `SEND_LIMIT` | The maximum number of emails to send in a single test run | **No** |

(if you're running this on windows make sure [Docker desktop](https://www.docker.com/products/docker-desktop/) is installed and running )

afterwards run.

```bash
  docker compose up
```

congratulations the project should now be up and running.

