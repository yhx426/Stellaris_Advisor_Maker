**用于快速制作《群星》游戏中的语音顾问Mod的工具**

1	文件夹下应包含3个内容	
		
		a.Config.csv配置表：里面配置音乐文件和事件的对应关系（原本用的是excel文件，但打包时需要Pandas库，太大了，改为csv文件，完全可以用excel文件导出为csv使用）
		b.Res文件夹：里面放置你的配音文件，文件为wav格式
		c.Advisor_Maker.exe程序（或py文件）
		
		
		
2	配置表怎么配？	
		![image](https://github.com/user-attachments/assets/ecae86d9-7abb-44a4-90be-f3d5bae90aab)




	每一行代表一个配音，具体需要多少行没有限制，完全看制作需要自行删减即可（默认的表是有58种事件，每种事件3个配音，随机播放1个）	
	接下来解释一下每个字段（也就是第一行的标题）是什么意思：	
	注意当前只有：英文标题的列是有用的，其他都是备注辅助用的，删掉也不影响，新增一些备注列也没问题（不重名即可）	
		
		序号：统计有多少个配音
		SoundType：P社定的事件类型，可在代码枚举中寻找，根据你的需求和后续游戏更新，可自由增减，若减少，则对应事件会播放默认的语音
		SoundFile：P社定的音频文件名字，同上
		事件类型备注：用于说明SoundType和SoundFile用处的
		
		台词范例：就是例子，没用，方便写台词用的
		Count：同种事件若有多个，需要计数区分，如图中的前3行，相当于制作了3个开场白配音，所以Count依次为1、2、3，这个不固定，你想做几个都可以，删除或复制新增一行即可
		Weights：同种事件若有多个，每次触发会随机播放一个，随机概率用这里控制，越大出现的频率越高
		台词：就是台词~~~没用，方便制作用的
		ResFileName：Res文件夹中，对应配音文件的文件名称，随便修改，但文件格式应为wav
		
		
3	Res文件夹:放置你的配音文件即可	
		![image](https://github.com/user-attachments/assets/483de197-a0e5-40d8-ae9b-95b77ef9ced6)

	
4	完成配置表和配音文件后	
		
	运行Advisor_Maker.exe程序	
	依照提示输入角色的 英文名 和 中文名称（注意英文名称不要带一些奇怪的符号，因为会用于代码，怕出错）	
		
		
		
5	运行完成后 会生成一个文件夹，里面包含3个文件夹，将他们复制到你在P社启动器中新建的Mod中	
		![image](https://github.com/user-attachments/assets/d0cd1801-49a9-4fef-aeb8-fd1503522136)

	
	然后添加一张封面图片	
		
![image](https://github.com/user-attachments/assets/08d219ff-d646-40e6-ace8-ff68e3589db9)


		
	在这里添加一个游戏中选择列表用的头像Icon图片 注意：需要为dds格式（dds格式怎么获取？随便网上找个在线转化工具，用png转化一下就好了）	
	Icon图片名字和你的人物英文名一致	
![image](https://github.com/user-attachments/assets/0338f30a-c44f-4b3e-b79d-f6199482ad3d)

		
6	到此应该大功告成了！	
