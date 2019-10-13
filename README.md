# Helpdesk Auto Ticket Classifier App

This is V0.1 of the App.
Future releases will integrate with leading helpdesk systems and automatically classify all incoming tickets.
Current release supports

- Flask app using MySQL DB as the backend
- Integration with Stripe to enable Card payments
- Inference (Ticket Classification) using saved pickle model
- Once payment is made, User can input Ticket Details and Classify ticket and assign to respective group
- The Ticket Categories are
  {0: 'ACCESS',
  1: 'HARDWARE',
  2: 'SOFTWARE',
  3: 'WINDOWS',
  4: 'EMAIL',
  5: 'ANTIVIRUS'
  }

## Examples

- Need to install Microsoft Office
- My monitor is showing lines and flickering
- I am getting blue screen. WHat should I do
- Unable to access login
- Email not working. Unable to send or receive emails
- How can I prevent virus attacks

## Screenshots

![Home Screen](https://github.com/rajesh1402/Helpdesk-Auto-Ticket-Classifier-App/tree/master/static/img/Home.png)
![Payment Screen](https://github.com/rajesh1402/Helpdesk-Auto-Ticket-Classifier-App/tree/master/static/img/Payment.png)
![Classify Ticket Screen](https://github.com/rajesh1402/Helpdesk-Auto-Ticket-Classifier-App/tree/master/static/img/ClassifyTicket.png)

## Thanks

I referred multiple github repos and tutorials to get this working.
Thanks to all of them. Will update the key ones in the near future.
