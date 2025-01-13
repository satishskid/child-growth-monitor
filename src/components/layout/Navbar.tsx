import React from 'react';
import Link from 'next/link';
import { FiSun, FiMoon } from 'react-icons/fi';
import { useTheme } from '../../hooks/useTheme';

const Navbar: React.FC = () => {
  const { theme, toggleTheme } = useTheme();

  return (
    <nav className="fixed top-0 left-0 right-0 bg-white dark:bg-gray-800 shadow-md z-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-16">
          <div className="flex items-center">
            <Link href="/" className="flex-shrink-0 flex items-center">
              <span className="text-2xl font-bold text-blue-600 dark:text-blue-400">
                Child Growth Monitor
              </span>
            </Link>
          </div>

          <div className="flex items-center">
            <button
              onClick={toggleTheme}
              className="p-3 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors duration-150"
              aria-label="Toggle theme"
            >
              {theme === 'dark' ? (
                <FiSun className="w-6 h-6 text-yellow-400" />
              ) : (
                <FiMoon className="w-6 h-6 text-gray-600" />
              )}
            </button>
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
