import React, { useState, useEffect } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import NotFound from "../Nopage/NotFound";
import CoursesNavbar from "../Navbar/TryCoursesNavbar";

export default function Courses() {
  const navigate = useNavigate();
  const [courses, setCourses] = useState([]);
  const [datafetched, setdatafetched] = useState(false);
  const [filteredCourses, setFilteredCourses] = useState([]);
  const [isloading, setisloading] = useState(true);

  useEffect(() => {
    const getData = async () => {
      try {
        let res = await axios.get("http://localhost:3001/auth/getAllCourse");
        if (res.data) {
          const allCourses = res.data.data;
          const limitedCourses = allCourses.slice(0, 2); // Show only two courses
          setCourses(limitedCourses);
          setFilteredCourses(limitedCourses);
          setisloading(false);
          setdatafetched(true);
        }
      } catch (err) {
        setisloading(false);
      }
    };
    getData();
    sessionStorage.removeItem("CourseID");
    sessionStorage.removeItem("CourseName");
    sessionStorage.removeItem("CourseUserID");
  }, []);

  return (
    <>
      <div className="bg-gray-900 text-white">
        <CoursesNavbar />
        <div className="text-center mt-8">
          <h2 className="text-3xl bg-gray-900 text-white font-semibold">
            Try Courses
          </h2>
        </div>
      </div>
      <div className="bg-gray-900 text-white min-h-screen flex flex-col items-center">
        <div className="w-full p-4 sm:p-10">
          {datafetched && filteredCourses?.length === 0 && <NotFound />}
          {isloading && <div className="spinner text-center" />}
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-8 justify-center">
            {filteredCourses?.map((c) => {
              return (
                <div
                  key={c?._id}
                  className="home-card rounded-lg overflow-hidden shadow-lg bg-gray-800"
                  style={{
                    borderRadius: 20,
                    minHeight: '500px',
                    minWidth: '500px',
                    margin: '0 auto',
                  }}
                  onClick={() => {
                    sessionStorage.setItem("CourseID", c._id);
                    sessionStorage.setItem("CourseUserID", c.userID);
                    sessionStorage.setItem("CourseName", c.title);
                    navigate("/coursedocs");
                  }}
                >
                  <img
                    src={c?.imageLink}
                    alt="Placeholder"
                    className="w-full"
                    style={{ maxHeight: '260px' }}
                  />
                  <div className="p-4">
                    <div
                      className="flex"
                      style={{
                        display: "flex",
                        justifyContent: "space-between",
                      }}
                    >
                      <h3 className="text-lg font-semibold mb-2">
                        {"@" + c?.userName + "/" + c?.title}
                      </h3>
                    </div>
                    <p className="text-gray-400">
                      {c?.description?.substring(0, 150)}
                    </p>
                  </div>
                </div>
              );
            })}
          </div>
        </div>
        <button
          className="mt-8 bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
          onClick={() => navigate("/auth")}
        >
          Access All Courses and Contribute
        </button>
      </div>
    </>
  );
}
