import React, { useState } from "react";
import Docum from "./Docum";
import DocumContent from "./DocumContent";
import TryCoursesNavbar from "../Navbar/TryCoursesNavbar";
import CoursesVideotab from "./Videotab";
import ProjectTabs from "./ProjectTabs";
import NotesTabs from "./NotesTabs";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faBook,
  faDiagramProject,
  faNoteSticky,
  faVideo,
} from "@fortawesome/free-solid-svg-icons";

export default function TryCourseTabs({ selectedDocs, setselectedDocs }) {
  const [tab, settab] = useState(false);
  const [activeTab, setActiveTab] = useState("documentation");

  const handleTabClick = (tabName) => {
    setActiveTab(tabName);
  };

  return (
    <>
      <div className="bg-gray-900 text-white min-h-screen">
        <TryCoursesNavbar />
        <div className="text-center text-3xl mb-10">{sessionStorage.getItem('CourseName')}</div>
        <div className="flex justify-center flex-wrap gap-4 sm:gap-8">
          <div
            className={`${
              activeTab === "documentation" ? "bg-gray-700" : "bg-gray-800"
            } hover:bg-gray-800 rounded p-4 text-center transition duration-300 ease-in-out w-32 h-32 flex flex-col items-center justify-center cursor-pointer`}
            onClick={() => handleTabClick("documentation")}
          >
            <FontAwesomeIcon icon={faBook} className="fa-2x mb-2" />
            <div className="text-lg">Documentation</div>
          </div>

          <div
            className={`${
              activeTab === "video" ? "bg-gray-700" : "bg-gray-800"
            } hover:bg-gray-800 rounded p-4 text-center transition duration-300 ease-in-out w-32 h-32 flex flex-col items-center justify-center cursor-pointer`}
            onClick={() => handleTabClick("video")}
          >
            <FontAwesomeIcon icon={faVideo} className="fa-2x mb-2" />
            <div className="text-lg">Video</div>
          </div>
          <div
            className={`${
              activeTab === "project" ? "bg-gray-700" : "bg-gray-800"
            } hover:bg-gray-800 rounded p-4 text-center transition duration-300 ease-in-out w-32 h-32 flex flex-col items-center justify-center cursor-pointer`}
            onClick={() => handleTabClick("project")}
          >
            <FontAwesomeIcon icon={faDiagramProject} className="fa-2x mb-2" />
            <div className="text-lg">Project</div>
          </div>
          <div
            className={`${
              activeTab === "notes" ? "bg-gray-700" : "bg-gray-800"
            } hover:bg-gray-800 rounded p-4 text-center transition duration-300 ease-in-out w-32 h-32 flex flex-col items-center justify-center cursor-pointer`}
            onClick={() => handleTabClick("notes")}
          >
            <FontAwesomeIcon icon={faNoteSticky} className="fa-2x mb-2" />
            <div className="text-lg">Notes</div>
          </div>
          
        </div>

        <div className="flex justify-center space-x-4 mt-3">
          {activeTab === "documentation" ? (
            !tab ? (
              <Docum setselectedDocs={setselectedDocs} settab={settab} />
            ) : (
              <DocumContent selectedDocs={selectedDocs} settab={settab} />
            )
          ) : activeTab === "video" ? (
            <CoursesVideotab />
          ) : activeTab === "project" ? (
            <ProjectTabs />
          ) : activeTab === "notes" ? (
            <NotesTabs />
          ) :(
            ""    
          )}
        </div>
      </div>
    </>
  );
}
