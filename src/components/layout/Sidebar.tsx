import React from 'react';
import Link from 'next/link';
import { useRouter } from 'next/router';
import { FiHome, FiUsers, FiBarChart2, FiPieChart, FiEdit } from 'react-icons/fi';

const navigation = [
  { name: 'Dashboard', href: '/', icon: FiHome },
  { name: 'Children Data', href: '/children', icon: FiUsers },
  { name: 'Statistics', href: '/statistics', icon: FiBarChart2 },
  { name: 'Visualizations', href: '/visualizations', icon: FiPieChart },
  { name: 'Data Entry', href: '/data-entry', icon: FiEdit },
];

const Sidebar: React.FC = () => {
  const router = useRouter();

  return (
    <div className="fixed left-0 top-16 h-full w-64 bg-white dark:bg-gray-800 shadow-lg">
      <nav className="mt-5 px-4">
        <div className="space-y-2">
          {navigation.map((item) => {
            const isActive = router.pathname === item.href;
            const Icon = item.icon;
            
            return (
              <Link
                key={item.name}
                href={item.href}
                className={`
                  flex items-center px-4 py-3 text-base font-medium rounded-lg transition-colors duration-150
                  ${isActive
                    ? 'bg-blue-100 text-blue-700 dark:bg-blue-900 dark:text-blue-200'
                    : 'text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-700'
                  }
                `}
              >
                <Icon className={`
                  h-6 w-6 mr-3
                  ${isActive
                    ? 'text-blue-700 dark:text-blue-200'
                    : 'text-gray-500 dark:text-gray-400'
                  }
                `} />
                {item.name}
              </Link>
            );
          })}
        </div>
      </nav>
    </div>
  );
};

export default Sidebar;
