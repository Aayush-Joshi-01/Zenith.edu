import React, { useState } from 'react';

const Forum = () => {
  const [questions, setQuestions] = useState([]);
  const [currentQuestion, setCurrentQuestion] = useState('');
  const [replyText, setReplyText] = useState('');

  const handleAskQuestion = () => {
    console.log('Asked Question:', currentQuestion);
    const newQuestion = { question: currentQuestion, replies: [] };
    setQuestions([...questions, newQuestion]);
    setCurrentQuestion('');
  };

  const handleReply = (index) => {
    console.log('Replied:', replyText);
    const updatedQuestions = [...questions];
    updatedQuestions[index].replies.push({ text: replyText, upvotes: 0, downvotes: 0 });
    setQuestions(updatedQuestions);
    setReplyText('');
  };

  const handleUpvote = (questionIndex, replyIndex) => {
    const updatedQuestions = [...questions];
    const reply = updatedQuestions[questionIndex].replies[replyIndex];

    if (reply.downvotes > 0) {
      reply.downvotes -= 1;
    }
    reply.upvotes += 1;

    setQuestions(updatedQuestions);
  };

  const handleDownvote = (questionIndex, replyIndex) => {
    const updatedQuestions = [...questions];
    const reply = updatedQuestions[questionIndex].replies[replyIndex];

    if (reply.upvotes > 0) {
      reply.upvotes -= 1;
    }
    reply.downvotes += 1;

    setQuestions(updatedQuestions);
  };

  return (
    <>
      <div className="p-4 bg-gray-900 text-white mb-6 border mt-6 rounded-lg" style={{ width: '60%' }}>
        <div className="p-6 rounded-lg shadow-md mb-4 bg-gray-900 text-white">
          <h2 className="text-2xl font-semibold mb-4">Ask a Question</h2>
          <textarea
            className="w-full p-2 border rounded-md"
            rows="4"
            placeholder="Type your question here..."
            value={currentQuestion}
            onChange={(e) => setCurrentQuestion(e.target.value)}
            style={{ color: '#000' }}
          ></textarea>
          <button
            className="mt-4 text-white py-2 px-4 rounded-md"
            onClick={handleAskQuestion}
            style={{
              background: '#9135db',
              transition: 'background 0.3s', // Adding a transition for smooth effect
            }}
            onMouseEnter={(e) => e.target.style.background = '#ad75da'} // Change color on hover
            onMouseLeave={(e) => e.target.style.background = '#9135db'}
          >
            Ask Question
          </button>
        </div>

        {questions.map((q, questionIndex) => (
          <div key={questionIndex} className="bg-grey-700 p-6 mt-5 border rounded-lg shadow-md mb-4 w-full">
            <h2 className="text-2xl font-semibold mb-4">Question</h2>
            <p>{q.question}</p>
            <div className="mt-4">
              <h3 className="text-xl font-semibold mb-2">Replies</h3>
              {q.replies.map((reply, replyIndex) => (
                <div key={replyIndex} className="mb-2 flex items-center justify-between">
                  <span>{reply.text}</span>
                  <div className="flex items-center">
                    <span className="mr-2">{reply.upvotes}</span>
                    <button
                      className="ml-2 text-white py-1 px-2 rounded-md flex items-center"
                      onClick={() => handleUpvote(questionIndex, replyIndex)}
                      style={{
                        background: '#9135db',
                        transition: 'background 0.3s', // Adding a transition for smooth effect
                      }}
                      onMouseEnter={(e) => e.target.style.background = '#ad75da'} // Change color on hover
                      onMouseLeave={(e) => e.target.style.background = '#9135db'}
                    >
                      👍
                    </button>
                    <span className="ml-2 mr-2">{reply.downvotes}</span>
                    <button
                      className="ml-2 text-white py-1 px-2 rounded-md flex items-center"
                      onClick={() => handleDownvote(questionIndex, replyIndex)}
                      style={{
                        background: '#9135db',
                        transition: 'background 0.3s', // Adding a transition for smooth effect
                      }}
                      onMouseEnter={(e) => e.target.style.background = '#ad75da'} // Change color on hover
                      onMouseLeave={(e) => e.target.style.background = '#9135db'}
                    >
                      👎
                    </button>
                  </div>
                </div>
              ))}
              <textarea
                className="w-full p-2 border rounded-md"
                rows="3"
                placeholder="Type your reply here..."
                value={replyText}
                onChange={(e) => setReplyText(e.target.value)}
                style={{ color: '#000' }}
              ></textarea>
              <button
                className="mt-4 text-white py-2 px-4 rounded-md"
                onClick={() => handleReply(questionIndex)}
                style={{
                  background: '#9135db',
                  transition: 'background 0.3s', // Adding a transition for smooth effect
                }}
                onMouseEnter={(e) => e.target.style.background = '#ad75da'} // Change color on hover
                onMouseLeave={(e) => e.target.style.background = '#9135db'}
              >
                Reply
              </button>
            </div>
          </div>
        ))}
      </div>
    </>
  );
};

export default Forum;
