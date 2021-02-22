/* FUNCTION FOR AUTOMATIC DELETE */
// Automatic download on page load

function automaticDownload() {
    var link = document.getElementById('downloadLink');

    link.download = 'download';

    link.click();
}
