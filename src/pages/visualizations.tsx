import React from 'react';
import Layout from '../components/layout/Layout';
import GrowthChart from '../components/charts/GrowthChart';

export default function Visualizations() {
  const heightData = {
    labels: [0, 12, 24, 36, 48, 60],
    datasets: [
      {
        label: 'Height (Boys)',
        data: [50, 75, 87, 96, 102, 108],
        borderColor: 'rgb(75, 192, 192)',
        fill: false,
      },
      {
        label: 'Height (Girls)',
        data: [49, 73, 85, 94, 100, 106],
        borderColor: 'rgb(255, 99, 132)',
        fill: false,
      },
    ],
  };

  const weightData = {
    labels: [0, 12, 24, 36, 48, 60],
    datasets: [
      {
        label: 'Weight (Boys)',
        data: [3.5, 9, 12, 14, 16, 18],
        borderColor: 'rgb(54, 162, 235)',
        fill: false,
      },
      {
        label: 'Weight (Girls)',
        data: [3.3, 8.5, 11.5, 13.5, 15.5, 17.5],
        borderColor: 'rgb(255, 159, 64)',
        fill: false,
      },
    ],
  };

  return (
    <Layout>
      <div className="space-y-6">
        <h1 className="text-3xl font-bold">Visualizations</h1>
        
        <div className="space-y-8">
          <div className="bg-white dark:bg-gray-800 shadow rounded-lg p-6">
            <h2 className="text-xl font-bold mb-4">Height Growth Charts</h2>
            <GrowthChart
              data={heightData}
              title="Height by Age and Gender"
              yAxisLabel="Height (cm)"
              whoStandards={[]}
            />
          </div>

          <div className="bg-white dark:bg-gray-800 shadow rounded-lg p-6">
            <h2 className="text-xl font-bold mb-4">Weight Growth Charts</h2>
            <GrowthChart
              data={weightData}
              title="Weight by Age and Gender"
              yAxisLabel="Weight (kg)"
              whoStandards={[]}
            />
          </div>
        </div>
      </div>
    </Layout>
  );
}
