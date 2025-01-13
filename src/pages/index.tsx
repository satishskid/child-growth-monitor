import React from 'react';
import Layout from '../components/layout/Layout';
import { FiUsers, FiTrendingUp, FiActivity, FiCalendar, FiPlus } from 'react-icons/fi';
import Link from 'next/link';

export default function Home() {
  const stats = [
    { name: 'Total Children', value: '42', icon: FiUsers, color: 'from-blue-500 to-blue-600' },
    { name: 'Average Height', value: '89 cm', icon: FiTrendingUp, color: 'from-emerald-500 to-emerald-600' },
    { name: 'Average Weight', value: '12.5 kg', icon: FiActivity, color: 'from-purple-500 to-purple-600' },
    { name: 'Last Updated', value: 'Today', icon: FiCalendar, color: 'from-amber-500 to-amber-600' },
  ];

  const recentChildren = [
    { 
      id: '1',
      name: 'John D.',
      age: '24 months',
      height: '87 cm',
      weight: '12 kg',
      trend: 'up',
      image: 'https://api.dicebear.com/7.x/avataaars/svg?seed=John',
      lastUpdate: '2025-01-13'
    },
    { 
      id: '2',
      name: 'Sarah M.',
      age: '36 months',
      height: '96 cm',
      weight: '14 kg',
      trend: 'up',
      image: 'https://api.dicebear.com/7.x/avataaars/svg?seed=Sarah',
      lastUpdate: '2025-01-13'
    },
    { 
      id: '3',
      name: 'Mike R.',
      age: '18 months',
      height: '82 cm',
      weight: '11 kg',
      trend: 'stable',
      image: 'https://api.dicebear.com/7.x/avataaars/svg?seed=Mike',
      lastUpdate: '2025-01-12'
    },
  ];

  return (
    <Layout>
      <div className="space-y-8">
        {/* Hero Section */}
        <div className="relative overflow-hidden rounded-2xl bg-gradient-to-r from-violet-600 to-indigo-600">
          <div className="absolute inset-0">
            <div className="absolute inset-0 bg-gradient-to-r from-violet-600 to-indigo-600 mix-blend-multiply" />
            <div className="absolute inset-0 bg-gradient-to-r from-transparent via-violet-900/50 to-transparent opacity-50" />
          </div>
          <div className="relative px-8 py-16">
            <div className="max-w-2xl">
              <h1 className="text-4xl font-bold tracking-tight text-white sm:text-5xl lg:text-6xl">
                Child Growth Monitor
              </h1>
              <p className="mt-6 max-w-xl text-lg text-indigo-100">
                Track and monitor children's growth with precision. Compare with WHO standards and ensure healthy development.
              </p>
              <div className="mt-8 flex gap-4">
                <Link
                  href="/data-entry"
                  className="inline-flex items-center rounded-lg bg-white px-6 py-3 text-sm font-semibold text-violet-600 shadow-sm hover:bg-violet-50 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white"
                >
                  <FiPlus className="mr-2 h-5 w-5" />
                  Add New Measurement
                </Link>
              </div>
            </div>
          </div>
        </div>

        {/* Stats Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          {stats.map((stat) => {
            const Icon = stat.icon;
            return (
              <div 
                key={stat.name}
                className="relative group"
              >
                <div className="absolute -inset-0.5 bg-gradient-to-r from-pink-600 to-purple-600 rounded-xl blur opacity-25 group-hover:opacity-50 transition duration-1000 group-hover:duration-200" />
                <div className="relative bg-white dark:bg-gray-800 rounded-xl shadow-xl p-6">
                  <div className="flex items-center justify-between">
                    <div className={`rounded-lg p-3 bg-gradient-to-r ${stat.color}`}>
                      <Icon className="h-6 w-6 text-white" />
                    </div>
                  </div>
                  <div className="mt-4">
                    <h3 className="text-lg font-medium text-gray-900 dark:text-white">{stat.name}</h3>
                    <p className="mt-2 text-3xl font-bold text-gray-900 dark:text-white">{stat.value}</p>
                  </div>
                </div>
              </div>
            );
          })}
        </div>

        {/* Recent Children */}
        <div className="bg-white dark:bg-gray-800 rounded-xl shadow-xl overflow-hidden">
          <div className="p-6">
            <div className="flex items-center justify-between mb-6">
              <h2 className="text-2xl font-bold text-gray-900 dark:text-white">Recent Children</h2>
              <Link
                href="/children"
                className="text-violet-600 hover:text-violet-500 font-medium"
              >
                View All
              </Link>
            </div>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              {recentChildren.map((child) => (
                <Link
                  key={child.id}
                  href={`/child/${child.id}`}
                  className="group relative bg-white dark:bg-gray-800 rounded-xl p-6 transition-all duration-300 hover:shadow-lg hover:-translate-y-1"
                >
                  <div className="flex items-start space-x-4">
                    <div className="flex-shrink-0 w-24 h-24">
                      <img
                        src={child.image}
                        alt={child.name}
                        className="w-full h-full rounded-xl object-cover bg-gray-100"
                      />
                    </div>
                    <div className="flex-1 min-w-0">
                      <h3 className="text-xl font-semibold text-gray-900 dark:text-white group-hover:text-violet-600 dark:group-hover:text-violet-400 mb-1">
                        {child.name}
                      </h3>
                      <div className="grid grid-cols-2 gap-4 mt-3">
                        <div>
                          <p className="text-sm text-gray-500 dark:text-gray-400">Age</p>
                          <p className="text-base font-medium text-gray-900 dark:text-white">{child.age}</p>
                        </div>
                        <div>
                          <p className="text-sm text-gray-500 dark:text-gray-400">Height</p>
                          <p className="text-base font-medium text-gray-900 dark:text-white">{child.height}</p>
                        </div>
                        <div>
                          <p className="text-sm text-gray-500 dark:text-gray-400">Weight</p>
                          <p className="text-base font-medium text-gray-900 dark:text-white">{child.weight}</p>
                        </div>
                        <div>
                          <p className="text-sm text-gray-500 dark:text-gray-400">Status</p>
                          <span className={`
                            inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium
                            ${child.trend === 'up' 
                              ? 'bg-green-100 text-green-800 dark:bg-green-800 dark:text-green-100'
                              : 'bg-blue-100 text-blue-800 dark:bg-blue-800 dark:text-blue-100'
                            }
                          `}>
                            {child.trend === 'up' ? '↑ Growing' : '→ Stable'}
                          </span>
                        </div>
                      </div>
                      <div className="mt-3 text-sm text-gray-500 dark:text-gray-400">
                        Last update: {child.lastUpdate}
                      </div>
                    </div>
                  </div>
                </Link>
              ))}
            </div>
          </div>
        </div>

        {/* Quick Actions */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {[
            {
              title: 'View Statistics',
              description: 'Analyze growth trends and patterns',
              href: '/statistics',
              gradient: 'from-pink-600 to-rose-600',
            },
            {
              title: 'Growth Charts',
              description: 'Visualize data with WHO standards',
              href: '/visualizations',
              gradient: 'from-violet-600 to-indigo-600',
            },
            {
              title: 'Add Data',
              description: 'Record new measurements',
              href: '/data-entry',
              gradient: 'from-blue-600 to-cyan-600',
            },
          ].map((action) => (
            <Link
              key={action.title}
              href={action.href}
              className="group relative"
            >
              <div className="absolute -inset-0.5 bg-gradient-to-r from-pink-600 to-purple-600 rounded-xl blur opacity-25 group-hover:opacity-75 transition duration-1000 group-hover:duration-200" />
              <div className="relative bg-white dark:bg-gray-800 rounded-xl shadow-xl p-6">
                <div className="bg-gradient-to-r ${action.gradient} bg-clip-text">
                  <h3 className="text-xl font-bold text-transparent bg-clip-text bg-gradient-to-r ${action.gradient} mb-2">
                    {action.title}
                  </h3>
                </div>
                <p className="text-gray-600 dark:text-gray-400">{action.description}</p>
              </div>
            </Link>
          ))}
        </div>
      </div>
    </Layout>
  );
}
