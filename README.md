# django-notification-gateway
Single service responsible for notifications by email, SMS, etc., abstracting authentication, retry logic and error handling via a RESTful API

## What is a Notification Gateway?
A notification gateway represents a single endpoint for notifying users or customers, abstracting the logic away from individual services such as: Customer portal, Billing, Marketing, Customer support, Internal admin panel, etc.

Without a notification gateway, every application would have to know how to send emails / SMS, how to authenticate with providers, and contain retrying and error handling logic. If one day we wished, for instance, to rely on a different email provider, we would need to change multiple points in the codebase(s), which is sloppy and error prone.

## Overall design
[Python 3](https://www.python.org/) back-end implemented using the [Django REST Framework]([https://www.django-rest-framework.org/).  
The design is based on a "wide services, thin views" architecture, where the former handle data integrity and behind-the-scenes domain logic, and the latter only handle HTTP concerns (extracting headers, returning JSON and status codes, etc.).  
More precisely, the code is structured as follows.

### Notification Service
The "brain" of the application, the Notification Service exports utility methods for the various operations within the Notification Gateway, e.g. dispatching a new notification, retry a failed one, sending the notification to the provider (see [**Provider Interface**](#provider-interface) section).

### Provider Interface
The Provider Interface stands between our application and the third-party service that will send our notification (e.g. SendGrid, Twilio, etc.,), ensuring a standardised access to all providers, regardless of implementation, and uniform feedback and error reporting back to the Notification Service (see [**Notification Service**](#notification-service) section).
