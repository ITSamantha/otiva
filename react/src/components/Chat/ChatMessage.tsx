import React from 'react';
import { Message } from '../../pages/Chat';

type ChatMessageProps = {
  message: Message;
  received?: boolean;
};

const ChatMessage = ({ message, received }: ChatMessageProps) => {
  return (
    <div className={'ChatMessage__Wrapper ' + (received ? '_received' : '_sent')}>
      <div className="ChatMessage">{message.text}</div>
    </div>
  );
};

export default ChatMessage;