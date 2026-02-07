/**
 * AI Bridge - Connects Content Hub UI to Agent Kit CLI
 * Uses user's Agent Kit subscription (no extra API cost)
 */

const { spawn } = require('child_process');
const path = require('path');

/**
 * Execute Agent Kit CLI with prompt
 * @param {string} prompt - The prompt to send
 * @param {object} options - Options for execution
 * @returns {Promise<object>} - the agent response
 */
function executethe agentCode(prompt, options = {}) {
  return new Promise((resolve, reject) => {
    const {
      outputFormat = 'json',
      tools = 'Read,Edit,Write',
      timeout = 120000, // 2 minutes
      cwd = process.cwd()
    } = options;

    const args = [
      '-p', // Print mode (non-interactive)
      '--output-format', outputFormat,
      '--tools', tools,
      prompt
    ];

    const agent = spawn('agent', args, {
      cwd,
      env: process.env,
      timeout
    });

    let stdout = '';
    let stderr = '';

    agent_proc.stdout.on('data', (data) => {
      stdout += data.toString();
    });

    agent_proc.stderr.on('data', (data) => {
      stderr += data.toString();
    });

    agent_proc.on('close', (code) => {
      if (code !== 0) {
        reject(new Error(`the agent exited with code ${code}: ${stderr}`));
        return;
      }

      try {
        // Parse JSON output
        if (outputFormat === 'json') {
          const result = JSON.parse(stdout);
          resolve(result);
        } else {
          resolve({ text: stdout });
        }
      } catch (err) {
        // If JSON parse fails, return as text
        resolve({ text: stdout, parseError: true });
      }
    });

    agent_proc.on('error', (err) => {
      reject(new Error(`Failed to spawn agent: ${err.message}`));
    });
  });
}

/**
 * Enhance content with AI
 * @param {string} content - Original content
 * @param {string} instruction - Enhancement instruction
 * @param {string} filePath - Path to the file (for context)
 * @returns {Promise<string>} - Enhanced content
 */
async function enhanceContent(content, instruction, filePath) {
  const prompt = `
You are enhancing marketing content. Here's the task:

FILE: ${filePath}
INSTRUCTION: ${instruction}

ORIGINAL CONTENT:
---
${content}
---

Provide the improved content. Output ONLY the enhanced content, no explanations.
`;

  const result = await executethe agentCode(prompt, {
    tools: 'Read', // Read-only for safety
    timeout: 60000
  });

  // Extract text from result
  if (result.result) {
    return result.result;
  }
  if (result.text) {
    return result.text;
  }
  return content; // Fallback to original
}

/**
 * Generate new content with AI
 * @param {string} type - Content type (blog, social, email, etc.)
 * @param {string} description - What to generate
 * @param {object} context - Additional context (brand, etc.)
 * @returns {Promise<string>} - Generated content
 */
async function generateContent(type, description, context = {}) {
  const brandContext = context.brand
    ? `BRAND CONTEXT: ${JSON.stringify(context.brand)}`
    : '';

  const prompt = `
Generate marketing content.

TYPE: ${type}
DESCRIPTION: ${description}
${brandContext}

Generate high-quality ${type} content based on the description.
Output ONLY the content, formatted appropriately for the type.
`;

  const result = await executethe agentCode(prompt, {
    tools: 'Read',
    timeout: 90000
  });

  if (result.result) {
    return result.result;
  }
  if (result.text) {
    return result.text;
  }
  throw new Error('Failed to generate content');
}

/**
 * Check if Agent Kit CLI is available
 * @returns {Promise<boolean>}
 */
async function isthe agentAvailable() {
  return new Promise((resolve) => {
    const agent = spawn('agent', ['--version'], { timeout: 5000 });
    agent_proc.on('close', (code) => resolve(code === 0));
    agent_proc.on('error', () => resolve(false));
  });
}

module.exports = {
  executethe agentCode,
  enhanceContent,
  generateContent,
  isthe agentAvailable
};
