var SpeechRecognition = window.webkitSpeechRecognition;
var recognition = new SpeechRecognition;

function speak() {
    recognition.start();
}

recognition.onresult = function(e) {
    conmsole.log(e);
    content = e.results[0][0].transcript;
    console.log(content);
    document.getElementById("textBox").innerHTML = content;

}