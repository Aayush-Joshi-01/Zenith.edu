import React, { useCallback } from "react";
import "react-toastify/dist/ReactToastify.css";
import { LineChart } from '@mui/x-charts/LineChart';
import { BarChart } from '@mui/x-charts/BarChart';

function AnalyticsModulate() {

      return (
        <>
        <div>
        <div className="flex flex-row">
            <div className="flex flex-col">
                <LineChart
                xAxis={[{ data: [1, 2, 3, 5, 8, 10] }]}
                series={[
                    {
                    data: [2, 5.5, 2, 8.5, 1.5, 5],
                    },
                ]}
                width={500}
                height={300}
                />
                <div>Views</div>
            </div>
            <div>
            <BarChart
            xAxis={[{ scaleType: 'band', data: ['Contributer 1', 'Contributer 2', 'Contributer 3'] }]}
            series={[{ data: [4, 3, 5] }, { data: [1, 6, 3] }, { data: [2, 5, 6] }]}
            width={500}
            height={300}
            />
                <div>Contributions</div>
            </div>
        </div>
        {/* <img src="https://github-readme-activity-graph.vercel.app/graph?username=Aayush-Joshi-01&radius=16&theme=dracula&area=true&order=5&hide_border=true&hide_title=false" height="300" alt="activity-graph graph"  /> */}
        </div>
        
        </>
      );
    }


export default AnalyticsModulate;
