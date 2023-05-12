// Define the base URL for the API
const apiUrl = "http://127.0.0.1:4557";

// Function to load all answers from the server
async function loadAll_Answers() {
  fetch(`${apiUrl}/answers`, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json'
    },
  })
    .then(response => response.json())
    .then(data => {
      console.log(data);
      // Add each answer to the answer list
      const answerList = document.getElementById('all_answers');
      answerList.innerHTML = ""
      for (const answerId in data) {
        const answer = data[answerId];
        let newAnswer = createAnswerElement(answer.answer, answer.points, answerId);
        answerList.appendChild(newAnswer);
      }
    })
    .catch(error => console.error('Error:', error));
}

// Function to update an appointment
async function completeAnswer(answerId, answer, points) {
  const ans = {
    answer: answer,
    points: points
  };
  // Make the API request to update the appointment
  const response = await fetch(`${apiUrl}/answers/${answerId}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(ans),
  });

  // Parse the response body as JSON
  const responseBody = await response.json();

  loadAll_Answers();

  // Log the response for debugging purposes
  console.log(responseBody);
}

// Function to delete all answers
async function deleteAnswer() {
  // Make the API request to delete the appointment
  const response = await fetch(`${apiUrl}/answers/{}`, {
    method: "DELETE",
  });

  // Parse the response body as JSON
  const responseBody = await response.json();

  loadAll_Answers();

  // Log the response for debugging purposes
  console.log(responseBody);
}

// Load all answers when the page is loaded
loadAll_Answers();

window.addEventListener("DOMContentLoaded", (event) => {
  const createAnswerForm = document.querySelector('#create-answer-form');
  // Get references to the HTML elements we need
  // const answerForm = document.getElementById("answer-form");
  const answerAnswerInput = document.getElementById("answer");
  const answerPointsInput = document.getElementById("points");

  if (createAnswerForm) {
    createAnswerForm.addEventListener("submit", createAnswer);
  }

  if (createAnswerForm) {
    createAnswerForm.addEventListener("submit", createAnswer);
  }

  // Function to create a new answer
  async function createAnswer(event) {
    // Prevent the default form submission behavior
    event.preventDefault();
    const form = event.target;
    const formData = new FormData(form);
    // Build the request body
    const answer = {
      answer: answerAnswerInput.value,
      points: answerPointsInput.value,
  
    };

    // Make the API request to create the new answer
    fetch(`${apiUrl}/answers`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(answer)
    })
      // Parse the response body as JSON
      .then(response => response.json())
      // Add the new appointment to the answer list
      .then(data => {
        loadAll_Answers();
        // Clear the form inputs
        answerAnswerInput.value = "";
        answerPointsInput.value = ""
        
      })
      .catch(error => console.error('Error:', error));
  }
});

// Function to create new answer element
function createAnswerElement(answer, points, id) {
  // Create a new list item
  let listItem = document.createElement('li');
  listItem.className = 'list-group-item d-flex justify-content-between align-items-center';

  // Create the answer answer element
  let answerAnswer = document.createTextNode(answer);

  // Create the answer points element
  let answerPoints = document.createElement('small');
  answerPoints.className = 'text-muted ml-2';
  answerPoints.innerText = points;

  // Create the delete button element
  let deleteButton = document.createElement('button');
  deleteButton.className = 'btn btn-sm btn-danger';
  deleteButton.innerText = 'Delete';
  deleteButton.addEventListener('click', function () {
    deleteAnswer(id);
  });


  // Add the appointment title to the list item
  listItem.appendChild(answerAnswer);
  listItem.appendChild(answerPoints);
  listItem.appendChild(deleteButton);


  // Return the list item element
  return listItem;
}