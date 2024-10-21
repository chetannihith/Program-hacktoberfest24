const textInput = document.getElementById("text-input");
const checkButton = document.getElementById("check-btn");
const result = document.getElementById("result");

checkButton.addEventListener("click",() => {
  const lowerReplaced = textInput.value.toLowerCase().replace(/[^A-Za-z0-9]/g,"")

  if(textInput.value === "") {
    alert("Please input a value")
  } else if(textInput.value.length === 1) {
    result.innerText = `${textInput.value} is a palindrome`
  } else if(lowerReplaced === [...lowerReplaced].reverse().join("")) {
    result.innerText = `${textInput.value} is a palindrome`
  }else {
    result.innerText = `${textInput.value} is not a palindrome`
  }
});
