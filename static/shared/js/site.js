function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
function deleteMethod() {
    var friendName = document.getElementById('friendName').value;
    var friendID = document.getElementById('friendID').value;
    var friendTag = document.getElementById('friendTag').value;
    var delete_confirmation = confirm('Are you sure you want to permanently delete this value?');
    if (delete_confirmation == true) {
        var providedUsername = prompt('Please enter the username of your discord friend');
        var providedTag = prompt('Please enter the tag of your discord friend');
        if (providedUsername == friendName && providedTag == friendTag) {
            console.log('This is working');
            console.log(csrftoken);
            fetch('/delete/' + friendID, {
                credentials: 'include',
                headers: {
                    'Content-type': 'application/json',
                    'X-CSRFToken': csrftoken
                },
                method: 'DELETE'
            });
            return window.location.assign('/');
        }
    }
}
