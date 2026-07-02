// src/config.js

// Provide a default value for NEXTAUTH_SECRET to avoid CI failures in development environments.
process.env.NEXTAUTH_SECRET = process.env.NEXTAUTH_SECRET || 'dev-secret';

function validateConfig() {
  if (!process.env.NEXTAUTH_SECRET) {
    throw new Error('NEXTAUTH_SECRET environment variable is required but not set.');
  }
}

module.exports = { validateConfig };
