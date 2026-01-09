document.addEventListener('DOMContentLoaded', function() {

  	// Use buttons to toggle between views
  	document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  	document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  	document.querySelector('#archived').addEventListener('click', () => load_mailbox('archived'));
  	document.querySelector('#compose').addEventListener('click', compose_email);

  	// By default, load the inbox
  	load_mailbox('inbox');
});


function compose_email() {

  	// Show compose view and hide other views
  	document.querySelector('#emails-view').style.display = 'none';
  	document.querySelector('#compose-view').style.display = 'block';
	document.querySelector('#email-detailed-view').style.display = 'none';

  	// Clear out composition fields
  	document.querySelector('#compose-recipients').value = '';
  	document.querySelector('#compose-subject').value = '';
  	document.querySelector('#compose-body').value = '';

	document.querySelector('#compose-form').onsubmit = send_email;
}

function send_email() {
	const error = document.querySelector('#error-message');
		if (error) {
			error.remove();
		}
		const to = document.querySelector('#compose-recipients');
		const subject = document.querySelector('#compose-subject');
		const body = document.querySelector('#compose-body');

		fetch('/emails', {
			method: 'POST',
			body: JSON.stringify({
				recipients: to.value,
				subject: subject.value,
				body: body.value
			})
		})
		.then(response => response.json().then(data => {
			return {
				status: response.status,
				data: data
			};
		}))
		.then(result => {
			if (result.status === 400) {
				const toDiv = document.querySelector('#compose-recipients').parentElement;
				const errorDiv = document.createElement('div');
				errorDiv.id = 'error-message';
				errorDiv.innerHTML = `${result.data.error}`;
				errorDiv.style.color = 'red';

				const form = document.querySelector('#compose-form');
				form.insertBefore(errorDiv, toDiv);
			} else {
				to.value = '';
				subject.value = '';
				body.value = '';
				console.log(result.data)
			}

			load_mailbox('sent')
		});

		return false;
}

function load_mailbox(mailbox) {

  	// Show the mailbox and hide other views
  	document.querySelector('#emails-view').style.display = 'block';
  	document.querySelector('#compose-view').style.display = 'none';
	document.querySelector('#email-detailed-view').style.display = 'none';

  	// Show the mailbox name
  	document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

	if (['inbox', 'sent', 'archived'].includes(mailbox)) {
		fetch(`/emails/${mailbox}`)
		.then(response => response.json())
		.then(emails => {
			emailView = document.querySelector('#emails-view')
			emails.forEach(email => {
				const emailBox = document.createElement('a');
				emailBox.classList.add('email-box');
				emailBox.onclick = () => load_email(email.id);

				if (email.read) {
					emailBox.style.backgroundColor = 'lightgray';
				}
				emailBox.innerHTML = `<b>${email.sender}</b> - ${email.subject} - ${email.timestamp}`;

				emailView.appendChild(emailBox);
			})
		});
	}
}

function load_email(email_id) {
	document.querySelector('#emails-view').style.display = 'none';
	document.querySelector('#compose-view').style.display = 'none';
	document.querySelector('#email-detailed-view').style.display = 'block';

	fetch(`/emails/${email_id}`)
	.then(response => response.json())
	.then(data => {
		const container = document.querySelector('#email-detailed-view');

		const subject = document.querySelector('#email-subject');
		subject.innerText = data.subject;

		const sender = document.querySelector('#email-sender');
		sender.innerHTML = `<b>From:</b> <i>${data.sender}</i>`;

		const recipients = document.querySelector('#email-recipients');
		recipients.innerHTML = `<b>To:</b> <i>${data.recipients}</i>`;

		const timestamp = document.querySelector('#email-timestamp');
		timestamp.innerText = data.timestamp;

		const content = document.querySelector('#email-content');
		content.innerText = data.body;

		const archiveButton = document.querySelector('#archive-button');
		if (data.archived) {
			archiveButton.innerText = 'Unarchive';
		}
		else {
			archiveButton.innerText = 'Archive';
		}
		archiveButton.onclick = function() {
			fetch(`/emails/${email_id}`, {
				method: 'PUT',
				body: JSON.stringify({
					archived: !data.archived
				})
			})
			.then(() => {
				load_mailbox('inbox');
			});
		}
		const replyButton = document.querySelector('#reply-button');
		replyButton.onclick = function() {
			compose_email();
			const subject = document.querySelector('#compose-subject');
			if (!data.subject.startsWith('Re: ')) {
				subject.value = 'Re: ' + data.subject;
			}
			else {
				subject.value = data.subject;
			}
			document.querySelector('#compose-recipients').value = data.sender;
			const body = document.querySelector('#compose-body')
			body.value = `"On ${data.timestamp} ${data.sender} wrote: ${data.body}"\n	\n`;
		}
	});

	fetch(`/emails/${email_id}`, {
		method: 'PUT',
		body: JSON.stringify({
			read: true
		})
	});
}
