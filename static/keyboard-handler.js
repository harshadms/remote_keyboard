var textbox;
var isCaps = false;
var lowercase = document.getElementsByClassName('lowercase-row');
var uppercase = document.getElementsByClassName('uppercase-row');
var event = new Event('change');

function typeVirtualKeyboardKey(key) {
	console.log(key);
	var key_val;
	if (textbox != null && key != 'Caps' && key != 'Shift') {
		if (key == 'Backspace') {
			textbox.value = textbox.value.substring(0, textbox.value.length - 1);
		} else if (key == 'Clear') {
			textbox.value = '';
		} else if (key == 'Tab') {
			textbox.value += '    ';
		} else if (key == 'Enter') {
			textbox.value += '\r';
		} else {
			if (key == '&lt;') {
				textbox.value += '<';
			} else if (key == '&gt;') {
				textbox.value += '>';
			} else if (key == '&amp;') {
				textbox.value += '&';
			} else {
				textbox.value += key;
			}
		}

		key_val = key;

		const request = new XMLHttpRequest();
		

		// $.getJSON('/test_keyboard_ctrl/' + key_val);
	}

	var requestURL = "/test_keyboard_ctrl/" + key;
	console.log(requestURL);
	const xhr = new XMLHttpRequest();
	xhr.open("GET", requestURL);
	xhr.send();
		
	if (key == 'Caps') {
			isCaps = !isCaps;
	}

	if (!isCaps) {
		for (row of lowercase) {
			row.style.display = 'block';
		}
		for (row of uppercase) {
			row.style.display = 'none';
		}
	} else {
		for (row of lowercase) {
			row.style.display = 'none';
		}
		for (row of uppercase) {
			row.style.display = 'block';
		}
	}

	if (key == 'Shift') {
		for (row of lowercase) {
			row.style.display = 'none';
		}
		for (row of uppercase) {
			row.style.display = 'block';
		}
	}
	if (textbox != null) {
		window.setTimeout(function ()
        {   
            textbox.dispatchEvent(event);
            textbox.focus();
		}, 0);
	}
	
}


function selectTextbox(newTextbox) {
	textbox = newTextbox;
}