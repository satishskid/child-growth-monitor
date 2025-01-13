import React from 'react';
import { useRouter } from 'next/router';
import Layout from '../../components/layout/Layout';
import { Line } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

// Mock data - replace with real data later
const childData = {
  id: '1',
  name: 'John Doe',
  birthDate: '2023-01-15',
  gender: 'Male',
  image: '/child-image.jpg',
  measurements: [
    { date: '2023-01-15', age: 0, height: 50, weight: 3.5 },
    { date: '2023-04-15', age: 3, height: 61, weight: 6.0 },
    { date: '2023-07-15', age: 6, height: 67, weight: 7.8 },
    { date: '2023-10-15', age: 9, height: 72, weight: 9.2 },
    { date: '2024-01-15', age: 12, height: 76, weight: 10.5 },
  ],
};

const ChildDetails = () => {
  const router = useRouter();
  const { id } = router.query;

  const chartOptions = {
    responsive: true,
    maintainAspectRatio: true,
    aspectRatio: 2, // This makes the chart shorter
    plugins: {
      legend: {
        position: 'top' as const,
        labels: {
          font: {
            size: 14, // Increased font size for legend
          },
        },
      },
      title: {
        display: true,
        text: 'Growth Trend',
        font: {
          size: 16, // Increased font size for title
        },
      },
    },
    scales: {
      y: {
        ticks: {
          font: {
            size: 12, // Increased font size for y-axis
          },
        },
        title: {
          display: true,
          text: 'Measurement',
          font: {
            size: 14, // Increased font size for axis title
          },
        },
      },
      x: {
        ticks: {
          font: {
            size: 12, // Increased font size for x-axis
          },
        },
        title: {
          display: true,
          text: 'Age (months)',
          font: {
            size: 14, // Increased font size for axis title
          },
        },
      },
    },
  };

  const heightData = {
    labels: childData.measurements.map(m => m.age),
    datasets: [
      {
        label: 'Height (cm)',
        data: childData.measurements.map(m => m.height),
        borderColor: 'rgb(53, 162, 235)',
        backgroundColor: 'rgba(53, 162, 235, 0.5)',
        tension: 0.3,
      },
    ],
  };

  const weightData = {
    labels: childData.measurements.map(m => m.age),
    datasets: [
      {
        label: 'Weight (kg)',
        data: childData.measurements.map(m => m.weight),
        borderColor: 'rgb(255, 99, 132)',
        backgroundColor: 'rgba(255, 99, 132, 0.5)',
        tension: 0.3,
      },
    ],
  };

  return (
    <Layout>
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8">
        {/* Child Info Header */}
        <div className="bg-gradient-to-r from-purple-600 to-indigo-600 rounded-xl shadow-2xl p-8">
          <div className="flex flex-col md:flex-row md:items-start md:justify-between gap-8">
            <div className="space-y-6">
              <div className="flex items-center space-x-6">
                <div className="w-32 h-32 rounded-xl overflow-hidden bg-white/20">
                  <img
                    src={childData.image || '/placeholder-child.png'}
                    alt={childData.name}
                    className="w-full h-full object-cover"
                  />
                </div>
                <div>
                  <h1 className="text-4xl font-bold text-white mb-2">{childData.name}</h1>
                  <div className="space-y-1">
                    <p className="text-lg text-purple-100">
                      <span className="font-medium">Born:</span> {childData.birthDate}
                    </p>
                    <p className="text-lg text-purple-100">
                      <span className="font-medium">Gender:</span> {childData.gender}
                    </p>
                  </div>
                </div>
              </div>
            </div>
            <div className="bg-white/20 backdrop-blur-lg rounded-xl p-6 min-w-[200px]">
              <p className="text-lg font-medium text-white mb-1">Current Age</p>
              <p className="text-4xl font-bold text-white">12 months</p>
            </div>
          </div>
        </div>

        {/* Latest Measurements */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div className="bg-white dark:bg-gray-800 rounded-xl shadow-xl p-6">
            <div className="text-center space-y-2">
              <h3 className="text-lg font-medium text-gray-500 dark:text-gray-400">Latest Height</h3>
              <p className="text-4xl font-bold text-gray-900 dark:text-white">76 cm</p>
              <p className="text-lg text-green-500">↑ 4cm from last measurement</p>
            </div>
          </div>
          <div className="bg-white dark:bg-gray-800 rounded-xl shadow-xl p-6">
            <div className="text-center space-y-2">
              <h3 className="text-lg font-medium text-gray-500 dark:text-gray-400">Latest Weight</h3>
              <p className="text-4xl font-bold text-gray-900 dark:text-white">10.5 kg</p>
              <p className="text-lg text-green-500">↑ 1.3kg from last measurement</p>
            </div>
          </div>
          <div className="bg-white dark:bg-gray-800 rounded-xl shadow-xl p-6">
            <div className="text-center space-y-2">
              <h3 className="text-lg font-medium text-gray-500 dark:text-gray-400">BMI</h3>
              <p className="text-4xl font-bold text-gray-900 dark:text-white">18.2</p>
              <p className="text-lg text-blue-500">Normal range</p>
            </div>
          </div>
        </div>

        {/* Growth Charts */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          <div className="bg-white dark:bg-gray-800 rounded-xl shadow-xl p-6">
            <h3 className="text-xl font-bold mb-4 text-gray-900 dark:text-white">Height Growth</h3>
            <div className="h-[300px]"> {/* Fixed height container */}
              <Line options={{...chartOptions, plugins: {...chartOptions.plugins, title: {display: false}}}} data={heightData} />
            </div>
          </div>
          <div className="bg-white dark:bg-gray-800 rounded-xl shadow-xl p-6">
            <h3 className="text-xl font-bold mb-4 text-gray-900 dark:text-white">Weight Growth</h3>
            <div className="h-[300px]"> {/* Fixed height container */}
              <Line options={{...chartOptions, plugins: {...chartOptions.plugins, title: {display: false}}}} data={weightData} />
            </div>
          </div>
        </div>

        {/* Measurement History */}
        <div className="bg-white dark:bg-gray-800 rounded-xl shadow-xl p-6">
          <h2 className="text-2xl font-bold mb-6 text-gray-900 dark:text-white">Measurement History</h2>
          <div className="overflow-x-auto">
            <table className="min-w-full divide-y divide-gray-200 dark:divide-gray-700">
              <thead>
                <tr>
                  <th className="px-6 py-3 text-left text-sm font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">Date</th>
                  <th className="px-6 py-3 text-left text-sm font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">Age (months)</th>
                  <th className="px-6 py-3 text-left text-sm font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">Height (cm)</th>
                  <th className="px-6 py-3 text-left text-sm font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">Weight (kg)</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-gray-200 dark:divide-gray-700">
                {childData.measurements.map((measurement, index) => (
                  <tr key={index} className="hover:bg-gray-50 dark:hover:bg-gray-700">
                    <td className="px-6 py-4 whitespace-nowrap text-base text-gray-900 dark:text-white">{measurement.date}</td>
                    <td className="px-6 py-4 whitespace-nowrap text-base text-gray-500 dark:text-gray-400">{measurement.age}</td>
                    <td className="px-6 py-4 whitespace-nowrap text-base text-gray-500 dark:text-gray-400">{measurement.height}</td>
                    <td className="px-6 py-4 whitespace-nowrap text-base text-gray-500 dark:text-gray-400">{measurement.weight}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </Layout>
  );
};

export default ChildDetails;
