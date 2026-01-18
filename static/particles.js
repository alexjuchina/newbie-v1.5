// 粒子背景效果实现
class ParticleBackground {
    constructor(canvas, particleCount = 100) {
        this.canvas = canvas;
        this.ctx = canvas.getContext('2d');
        this.particles = [];
        this.connections = [];
        this.width = window.innerWidth;
        this.height = window.innerHeight;
        this.mouse = { x: null, y: null }; // 鼠标位置
        
        // 配置参数
        this.config = {
            particleCount: particleCount,
            particleSize: 2,
            particleColor: 'rgba(37, 99, 235, 0.8)',
            connectionColor: 'rgba(37, 99, 235, 0.3)',
            connectionDistance: 150,
            particleSpeed: 0.5,
            attractionRadius: 150, // 增加鼠标吸引半径
            attractionStrength: 0.1, // 提高鼠标吸引力强度
        };
        
        this.init();
    }
    
    // 初始化画布和粒子
    init() {
        // 设置画布大小
        this.canvas.width = this.width;
        this.canvas.height = this.height;
        
        // 创建粒子
        for (let i = 0; i < this.config.particleCount; i++) {
            this.particles.push({
                x: Math.random() * this.width,
                y: Math.random() * this.height,
                vx: (Math.random() - 0.5) * this.config.particleSpeed,
                vy: (Math.random() - 0.5) * this.config.particleSpeed,
                size: this.config.particleSize
            });
        }
        
        this.animate();
        this.bindEvents();
    }
    
    // 动画循环
    animate() {
        // 清空画布
        this.ctx.clearRect(0, 0, this.width, this.height);
        
        // 更新和绘制粒子
        this.updateParticles();
        
        // 绘制连接线
        this.drawConnections();
        
        // 循环动画
        requestAnimationFrame(() => this.animate());
    }
    
    // 更新粒子位置
    updateParticles() {
        this.particles.forEach(particle => {
            // 鼠标吸引力
            if (this.mouse.x !== null && this.mouse.y !== null) {
                const dx = this.mouse.x - particle.x;
                const dy = this.mouse.y - particle.y;
                const distance = Math.sqrt(dx * dx + dy * dy);
                
                if (distance < this.config.attractionRadius) {
                    const force = (this.config.attractionRadius - distance) / this.config.attractionRadius * this.config.attractionStrength;
                    particle.vx += dx * force;
                    particle.vy += dy * force;
                }
            }
            
            // 更新位置
            particle.x += particle.vx;
            particle.y += particle.vy;
            
            // 速度限制
            const maxSpeed = this.config.particleSpeed * 3;
            particle.vx = Math.max(-maxSpeed, Math.min(maxSpeed, particle.vx));
            particle.vy = Math.max(-maxSpeed, Math.min(maxSpeed, particle.vy));
            
            // 边界检测
            if (particle.x < 0 || particle.x > this.width) {
                particle.vx *= -1;
            }
            if (particle.y < 0 || particle.y > this.height) {
                particle.vy *= -1;
            }
            
            // 绘制粒子
            this.ctx.fillStyle = this.config.particleColor;
            this.ctx.beginPath();
            this.ctx.arc(particle.x, particle.y, particle.size, 0, Math.PI * 2);
            this.ctx.fill();
        });
    }
    
    // 绘制粒子间的连接线
    drawConnections() {
        for (let i = 0; i < this.particles.length; i++) {
            for (let j = i + 1; j < this.particles.length; j++) {
                const dx = this.particles[i].x - this.particles[j].x;
                const dy = this.particles[i].y - this.particles[j].y;
                const distance = Math.sqrt(dx * dx + dy * dy);
                
                // 在指定距离内绘制连接线
                if (distance < this.config.connectionDistance) {
                    this.ctx.strokeStyle = this.config.connectionColor;
                    this.ctx.lineWidth = 0.5;
                    this.ctx.beginPath();
                    this.ctx.moveTo(this.particles[i].x, this.particles[i].y);
                    this.ctx.lineTo(this.particles[j].x, this.particles[j].y);
                    this.ctx.stroke();
                }
            }
        }
    }
    
    // 绑定事件
    bindEvents() {
        // 窗口大小调整
        window.addEventListener('resize', () => {
            this.width = window.innerWidth;
            this.height = window.innerHeight;
            this.canvas.width = this.width;
            this.canvas.height = this.height;
        });
        
        // 鼠标移动事件
        window.addEventListener('mousemove', (e) => {
            this.mouse.x = e.clientX;
            this.mouse.y = e.clientY;
        });
        
        // 鼠标离开窗口事件
        window.addEventListener('mouseleave', () => {
            this.mouse.x = null;
            this.mouse.y = null;
        });
    }
}

// 页面加载完成后初始化
window.addEventListener('DOMContentLoaded', () => {
    const canvas = document.getElementById('particle-canvas');
    if (canvas) {
        new ParticleBackground(canvas, 100); // 增加粒子数量到100个
    }
});