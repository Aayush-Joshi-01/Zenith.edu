import React, { useState, useEffect, useRef } from "react";

function CourseChat() {
  const [inputText, setInputText] = useState("");
  const [chatHistory, setChatHistory] = useState([]);
  const messagesEndRef = useRef(null);
  const chatContainerRef = useRef(null);

const courseId = sessionStorage.getItem("CourseID");
console.log(courseId); // Verify the courseId value

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  const fetchResponseFromAPI = async () => {
    try {
      const response = await fetch("http://localhost:5000/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          user_prompt: inputText,
          id: courseId, // Change 'course_id' to 'id'
          chat_history: chatHistory.map((message) => message.text),
        }),
      });
  
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
  
      const data = await response.json();
      return { response: data.response, updatedChatHistory: data.chat_history };
    } catch (error) {
      console.error("Error fetching data:", error);
      return { response: "Error fetching response.", updatedChatHistory: chatHistory };
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (inputText.trim() === "") return;

    const { response, updatedChatHistory } = await fetchResponseFromAPI();
    setChatHistory([...updatedChatHistory, { text: inputText, sender: "User" }, { text: response, sender: "ZenAI" }]);
    setInputText("");
  };

  useEffect(() => {
    scrollToBottom();
  }, [chatHistory]);

  return (
    <div className="flex flex-col w-full max-w-md mx-auto mt-8 h-[400px] border border-gray-300 rounded-lg overflow-hidden">
      <div
        className="flex-1 p-4 overflow-y-auto"
        ref={chatContainerRef}
        style={{ scrollBehavior: "smooth", overflow: "overlay" }}
      >
        {chatHistory.map((message, index) => (
          <div
            key={index}
            className={`my-2 ${message.sender === "User" ? "self-end" : "self-start"}`}
          >
            <div
              className={`p-2 rounded-lg ${message.sender === "User" ? "bg-blue-500 text-white" : "bg-white text-black"}`}
            >
              <p>{message.text}</p>
              <div className="flex justify-between mt-2">
                <p className="text-xs text-white-500">{new Date().toLocaleTimeString()}</p>
                <p className="text-xs font-semibold">{message.sender}</p>
              </div>
            </div>
          </div>
        ))}
        <div ref={messagesEndRef} />
      </div>
      <div className="bg-gray-800 p-4" style={{ height: "75px" }}>
        <div className="flex">
          <input
            type="text"
            value={inputText}
            placeholder="Type your question..."
            onChange={(e) => setInputText(e.target.value)}
            className="flex-1 p-2 mr-2 border rounded"
            style={{ width: "400px", color: "#000" }}
            onKeyDown={(e) => e.key === "Enter" && handleSubmit(e)}
          />
          <button
            onClick={handleSubmit}
            className="bg-blue-500 text-white p-2 rounded"
            style={{ background: "#9135db" }}
          >
            &#9658;
          </button>
        </div>
      </div>
    </div>
  );
}

export default CourseChat;
