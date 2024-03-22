const checkBox = document.querySelector("#check");
const password = document.querySelector("input[type='password']");
function togglePassword() {
    if (checkBox.checked) {
        password.type = "text";
    } else {
        password.type = "password";
    }
}
    checkBox.addEventListener("click", togglePassword)

